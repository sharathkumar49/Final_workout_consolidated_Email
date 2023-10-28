

import os

for tester in ['Alpar Wonerth', 'Anett Rau', 'Annette Opitz', 'Barbara Kronmueller', 'Chinmay Shah', 'Eric Schnurr', 'Florian Brenner', 'Gunasekaran Loganathan', 'Karthick Jayachandran', 'Nagarampalli Kalyan', 'Pavan Palreddygari', 'Robin Mai', 'Sharath Muthu', 'Simone Klasmeier', 'Thanusha Koparthy', 'Unni Rajanarayanan', 'Vijayalakshmi R']:
    if os.path.exists("./templates/{}_section1.html".format(str(tester).replace(' ','_'))):
        os.remove("./templates/{}_section1.html".format(str(tester).replace(' ','_')))

    if os.path.exists("./templates/{}_section2.html".format(str(tester).replace(' ','_'))):
        os.remove("./templates/{}_section2.html".format(str(tester).replace(' ','_')))
    
    if os.path.exists("./templates/{}_section3.html".format(str(tester).replace(' ','_'))):
        os.remove("./templates/{}_section3.html".format(str(tester).replace(' ','_')))

    if os.path.exists("./templates/{}_section4.html".format(str(tester).replace(' ','_'))):
        os.remove("./templates/{}_section4.html".format(str(tester).replace(' ','_')))

    if os.path.exists("./single_tester_data/{}_final.html".format(str(tester).replace(' ','_'))):
        os.remove("./single_tester_data/{}_final.html".format(str(tester).replace(' ','_')))

    if os.path.exists("./templates/all_testers_final.html"):
        os.remove("./templates/all_testers_final.html")
    
    if os.path.exists("./comprehensive_tester_data/comprehensive_final.html"):
        os.remove("./comprehensive_tester_data/comprehensive_final.html")

    if os.path.exists("./templates/exceptiontable.html".format(str(tester).replace(' ','_'))):
        os.remove("./templates/exceptiontable.html".format(str(tester).replace(' ','_')))
    