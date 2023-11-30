import csv
import os
from datetime import date, datetime
from database import Member,Show,Venue
from celery.schedules import crontab
from jinja2 import Template
from mail_config import send_email
from weasyprint import HTML

from app import celery,cache


# @celery.on_after_finalize.connect
# def setup_intervalTASK(sender, **kwargs):
#     sender.add_periodic_task(
#         # Send a remainder at 5:30pm IST of every day
#         # crontab(minute=30, hour=17),
#         180,
#         daily_rem.s(), name="Daily reminder"
#     )

#     sender.add_periodic_task(
#         # Send the monthly report at 5:30pm IST of every month
#         # crontab(minute=30, hour=17, day_of_month=25),
#         180,
#         monthly_report.s(), name="Monthly Report"
#     )

@celery.task()
@cache.memoize(timeout=15)
def ex_report(venue_id: int):
    filepath = 'static/download/'+str(venue_id)+'_venue_details.csv'

    # Check if folder is not present then create one
    if not os.path.exists('static/download/'):
        os.mkdir(path='static/download/')
    # Create the csv file
    with open(file=filepath, mode='w') as file:
        csv_obj = csv.writer(file, delimiter=',')
        csv_obj.writerow(['venue id','venue name','capacity','Place','Number of Shows'])
        data = Venue.query.filter_by(ID=venue_id).first()
        csv_obj.writerow([data.ID,data.Name,data.Capacity,data.Place,len(data.shows)])

    with open(r"templates/download.html") as file:
        msg_template = Template(file.read())
    
    send_email(to=data.Admin, subject="CSV file for Venue report",
                msg=msg_template.render(username=data.Admin,name=data.Name), attachment=filepath)
    return 'sucess'




@celery.task()
def daily_rem():
    print("in reminder")
    users = list(filter(lambda x:len(x.movie_list)!= 0 , Member.query.all()))
    for user in users:
        username = user.Name
        print(user.movie_list)
        show_id = list(map(lambda x:x.Show_ID,user.movie_list))
        show_name = [Show.query.filter_by(ID = x).first().Name for x in show_id ]
        print(show_name)
        with open(r"templates/daily_reminder.html") as file:
            msg_template = Template(file.read())
        send_email(to=user.email_ID, subject="Daily reminder",
                   msg=msg_template.render(username=username, movie_name=','.join(show_name)))
    return 'sucess'

@celery.task()
def monthly_report():
    users = Member.query.all()
    month = date.today().strftime("%B")
    for user in users:
        filepath = f"static/monthly_report/monthlyreport{str(user.email_ID)}_{month}.pdf"
        show_id = list(map(lambda x:x.Show_ID,user.movie_list))
        data = []
        for i in show_id:
            x = {}
            movie = Show.query.filter_by(ID=i).first()
            x['id']=i
            x['movie_name'] = movie.Name
            x['rating'] = movie.Rating
            x['price'] = movie.Ticket_Price
            data.append(x)

        with open(r"templates/monthly_report.html") as file:
            msg_template = Template(file.read())
        with open(r"templates/pdf.html") as file:
            pdf_template = Template(file.read())
        pdf_html = HTML(string=pdf_template.render(username=user.Name,month=month,data = data))
        pdf_html.write_pdf(target=filepath)

        send_email(to=user.email_ID, subject="Monthly report", attachment=filepath,
                   msg=msg_template.render(username=user.Name))
        
    return 'sucess'