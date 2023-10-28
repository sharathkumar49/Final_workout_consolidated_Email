

from jinja2 import Environment, FileSystemLoader
import os
import jinja2
import time

#exception
exception_dict = {'Others': [{'name': 'MRN R15.1.0 Distribution Hub', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 Distribution Hub', 'owner': 'Noowner', 'reason': ''}, {'name': 'R15.1.0 poll NE build url', 'owner': 'Noowner', 'reason': ''}, {'name': 'R15.1.0 poll GMRE build url', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 new GMRE Build Trigger', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 FlexOT Trigger', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 new NE build Trigger', 'owner': 'Noowner', 'reason': ''}], 'Scratch Jobs': [{'name': 'MRN R15.1.0 ADD4 LBand Scratch Installation', 'owner': 'Barbara Kronmueller', 'reason': ''}, {'name': 'MRN R15.1.0 ADD4 and Cluster Scratch Installation', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'MRN R15.1.0 ADD4 and Cluster Scratch Installation for Regression', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'MRN R15.1.0 Mixed PSS24x12x8x and Cluster Scratch Installation', 'owner': 'Noowner', 'reason': ''}, {'name': 'MRN R15.1.0 ADD6 Scratch Installation', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG Scratch Installation', 'owner': 'Noowner', 'reason': ''}], 'Hardware Profiles': [{'name': 'HW R15.1.0 ADD4 CDCMetal APT batch', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'HW R15.1.0 ADD5U 3R CDCMetal APT batch', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'HW R15.1.0 ADD5U CDCMetal APT batch', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'HW R15.1.0 MRN-24x CDCMetal APT batch', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'HW R15.1.0 WDM CDC-Diamond LSP Lifecycle S6AD600L_SFM6L_SBR', 'owner': 'Chinmay Shah', 'reason': ''}], 'Isug Testing': [{'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1205 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1300 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1304 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1310 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1400 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1408 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1410 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1500 to 1510', 'owner': 'Noowner', 'reason': ''}]}


for exceptionGroup in exception_dict:
    print("\nexceptionGroup:", exceptionGroup)
    for singleexception in exception_dict[exceptionGroup]:
        print("\nsingleexception",singleexception)


if exception_dict:
    env = jinja2.Environment(loader = FileSystemLoader("templates/"))
  
    context = {"exceptionData": exception_dict}
    template = env.get_template("portionofconsolidatedMail5.html")
    output = template.render(context)

    with open("./templates/exceptiontable.html","a") as fileop:
        fileop.write(output)

    print("\nFinished adding data for section 3")
    time.sleep(30)