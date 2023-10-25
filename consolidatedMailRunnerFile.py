


#from smtplib import SMTP 
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import os
import jinja2


Final_nested_dict = {'Barbara Kronmueller': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_jobs': 0, 'red_jobs_list':[], 'green_jobs':24, 'not_executed_jobs':2, 'not_executed_jobs_list':['MRN R15.1.0 ADD6 Alarm DAD2T6', 'MRN R15.1.0 ADD6 Alarm Test DMAT6']},{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_jobs': 0, 'red_jobs_list':[], 'green_jobs':24, 'not_executed_jobs':2, 'not_executed_jobs_list':['MRN R15.1.0 ADD6 Alarm DAD2T6', 'MRN R15.1.0 ADD6 Alarm Test DMAT6']}, {'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_jobs': 0, 'red_jobs_list':[], 'green_jobs':24, 'not_executed_jobs':2, 'not_executed_jobs_list':['MRN R15.1.0 ADD6 Alarm DAD2T6', 'MRN R15.1.0 ADD6 Alarm Test DMAT6']}]}

projdict_notexecuted = {'Barbara Kronmueller' : ['Mrn some profile under her name', 'wdm profile under her name']}


#env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))
env = jinja2.Environment(loader = FileSystemLoader("templates/"))
#context = {"movies": movies, "theatres": theatres, "actors" : actors, "title" : "working out"}
context = {"tester": 'Barbara Kronmueller', "MRNDATA" : Final_nested_dict['Barbara Kronmueller'], "projectsnotexecuted" : projdict_notexecuted['Barbara Kronmueller']}
print("\nhere priting context", context)
template = env.get_template("Mainportionofconsolidated.html")
print("\nhere printing template:", template)
output = template.render(context)
print("\nhere printing output:", output)


with open("finaloutput.html","w") as fileop:
    fileop.write(output)
