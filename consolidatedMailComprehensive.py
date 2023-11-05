


#from smtplib import SMTP 
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import os
import jinja2
import time


testers = ['Alpar Wonerth', 'Anett Rau', 'Annette Opitz', 'Barbara Kronmueller', 'Chinmay Shah', 'Eric Schnurr', 'Florian Brenner', 'Gunasekaran Loganathan', 'Karthick Jayachandran', 'Nagarampalli Kalyan', 'Pavan Palreddygari', 'Robin Mai', 'Sharath Muthu', 'Simone Klasmeier', 'Thanusha Koparthy', 'Unni Rajanarayanan', 'Vijayalakshmi R']


Final_nested_dict = {'Alpar Wonerth': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 Brownfield Migration'], 'green_jobs': 6, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 7, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 7, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 Alien Brownfield Migration'], 'green_jobs': 6, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 7, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Barbara Kronmueller': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 24, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 Alarm Test D6AD2T6', '  MRN R15.1.0 ADD6 Alarm Test DMAT6']}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 24, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 Alarm Test D6AD2T6', '  MRN R15.1.0 ADD6 Alarm Test DMAT6']}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 24, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 Alarm Test D6AD2T6', '  MRN R15.1.0 ADD6 Alarm Test DMAT6']}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 24, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 Alarm Test D6AD2T6', '  MRN R15.1.0 ADD6 Alarm Test DMAT6']}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 2, 'red_jobs_list': ['MRN R15.1.0 Plugging Tests', 'WDM R15.1.0 ODUonOT D5X500L on CDC L-C'], 'green_jobs': 22, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 Alarm Test D6AD2T6', '  MRN R15.1.0 ADD6 Alarm Test DMAT6']}], 'Chinmay Shah': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 ADD4 Alarm Test S4X400'], 'green_jobs': 6, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 2, 'red_jobs_list': ['MRN R15.1.0 ADD4 Alarm Test DFC12AB', '  MRN R15.1.0 ADD4 Alarm Test S4X400'], 'green_jobs': 4, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['MRN R15.1.0 ADD4 Alarm Test DFC12EAB']}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 S13X100 Alarm Tests'], 'green_jobs': 4, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['MRN R15.1.0 ADD4 Alarm Test S4X400', 'MRN R15.1.0 DFM6 Alarm_WSR_Prio_Maintenance Test']}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 ADD4 Alarm Test S4X400'], 'green_jobs': 6, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 2, 'red_jobs_list': ['MRN R15.1.0 ADD4 Alarm Test DFC12AB', '  MRN R15.1.0 ADD4 Alarm Test S4X400'], 'green_jobs': 4, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['MRN R15.1.0 ADD4 Alarm Test DFC12EAB']}], 'Eric Schnurr': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Florian Brenner': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 10, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 special tests APT batch']}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 3, 'red_jobs_list': ['MRN R15.1.0 ADD4 special tests APT batch', 'MRN R15.1.0 S6AD600 and SFM6 special tests APT batch', '  MRN R15.1.0 DFM6 special tests APT batch'], 'green_jobs': 6, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 special tests APT batch', 'MRN R15.1.0 S13X100 CDC tests APT batch']}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 3, 'red_jobs_list': ['MRN R15.1.0 DFM6 special tests APT batch', 'MRN R15.1.0 S6AD600 and SFM6 special tests APT batch', '  MRN R15.1.0 ASE Noise Segregation'], 'green_jobs': 7, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 special tests APT batch']}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 3, 'red_jobs_list': ['MRN R15.1.0 ADD4 special tests APT batch', 'MRN R15.1.0 DFM6 special tests APT batch', '  MRN R15.1.0 ASE Noise Segregation'], 'green_jobs': 7, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 special tests APT batch']}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 Cluster APT batch'], 'green_jobs': 6, 'not_executed_jobs': 4, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 special tests APT batch', 'MRN R15.1.0 DFM6 special tests APT batch', 'MRN R15.1.0 S13X100 CDC tests APT batch', '  MRN R15.1.0 ASE Noise Segregation']}], 'Karthick Jayachandran': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Nagarampalli Kalyan': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 FF3 Interworking'], 'green_jobs': 3, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Pavan Palreddygari': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Robin Mai': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 CSW Layer-1 LocalLSP'], 'green_jobs': 0, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 CSW Layer-1 LocalLSP'], 'green_jobs': 0, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 CSW Layer-1 LocalLSP'], 'green_jobs': 0, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 CSW Layer-1 LocalLSP'], 'green_jobs': 0, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Sharath Muthu': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 6, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 6, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 5, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['MRN R15.1.0 MRN-24x Improvements and PrioPreemption']}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 5, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['MRN R15.1.0 MRN-24x Improvements and PrioPreemption']}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 5, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['MRN R15.1.0 MRN-24x Improvements and PrioPreemption']}], 'Thanusha Koparthy': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['WDM R15.1.0 CSW Layer-1 OpenSNCP', 'WDM R15.1.0 CSW Oduptf Odukxc Databearer Indices Test']}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 OpenSNCP Layer1 LSP Tests'], 'green_jobs': 1, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['WDM R15.1.0 CSW Layer-1 OpenSNCP', 'WDM R15.1.0 CSW Oduptf Odukxc Databearer Indices Test']}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 3, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 CSW Oduptf Odukxc Databearer Indices Test']}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 3, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 CSW Oduptf Odukxc Databearer Indices Test']}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 3, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 CSW Oduptf Odukxc Databearer Indices Test']}], 'Unni Rajanarayanan': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 8, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 OPSUM']}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 8, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 OPSUM']}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 8, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 OPSUM']}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 8, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 OPSUM']}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 11DPM8_8P20_Unkeyed_Keyed'], 'green_jobs': 7, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 OPSUM']}], 'Vijayalakshmi R': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 Flex OT']}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 Flex OT']}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 DEGTRANS TEST'], 'green_jobs': 3, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 Flex OT']}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 Flex OT']}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 5, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}]}

Final_nested_dict_mrn ={'Alpar Wonerth': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Anett Rau': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 2, 'red_jobs_list': ['MRN R15.1.0 ADD4 S6AD600 SFM6 Ext for S5AD400H - Rob Maint PrioPreempt', 'MRN R15.1.0 MLN Prot TransMux FA-Term'], 'green_jobs': 10, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['MRN R15.1.0 ADD6 DMAT6 D6AD2T4H - Rob Maint PrioPreempt']}], 'Gunasekaran Loganathan': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 CDC-F_2.0_CL_IRDM20-32-32L-OMDCL_AND_OT_Direct_Connected_to_MXN'], 'green_jobs': 13, 'not_executed_jobs': 1, 'not_executed_jobs_list': ['WDM R15.1.0 CDC-F_2.0_CL_IRDM20-32-32L-OMDCL_AND_OT_Direct_Connected_to_MXN_ALARM']}], 'Karthick Jayachandran': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 3, 'red_jobs_list': ['MRN R15.1.0 1UX500 MR', 'MRN R15.1.0 1UX500 OPSUM', 'MRN R15.1.0 2UX500 MAINTENANCE AND ROBUSTNESS'], 'green_jobs': 9, 'not_executed_jobs': 3, 'not_executed_jobs_list': ['MRN R15.1.0 1UX500 Cluster', 'MRN R15.1.0 2UC1TL IW', 'MRN R15.1.0 2UX500 CLUSTER']}], 'Nagarampalli Kalyan': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 14, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Pavan Palreddygari': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 3, 'red_jobs_list': ['MRN R15.1.0 2UC1T WITHOUT CLUSTER', 'MRN R15.1.0 4UC1T CLUSTER', 'MRN R15.1.0 Alarm test with CDC config'], 'green_jobs': 10, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Robin Mai': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 MRN-24x12x8x Diversity Constraint Test'], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Sharath Muthu': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 5, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Simone Klasmeier': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 3, 'red_jobs_list': ['MRN R15.1.0 2UC1T Pure Layer0 and FF3 restrictions', 'MRN R15.1.0 S5AD400 Default LSP lifecycles', 'MRN R15.1.0 S6AD600L SFM6L Default LSP lifecycles'], 'green_jobs': 16, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Thanusha Koparthy': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 9, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Unni Rajanarayanan': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 6, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Vijayalakshmi R': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 OPSUML S6AD600L_SFM6L LSP Lifecycles'], 'green_jobs': 16, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}]}

Final_nested_dict_manual = {'Annette Opitz': [{'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['TEST IR4 R15.1.0 APT CLI ANV 22.12.00', 'TEST IR4 R15.1.0 APT CLI ANV 23.12.0']}], 'Chinmay Shah': [{'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 1, 'red_jobs_list': ['HW R15.1.0 WDM CDC-Diamond LSP Lifecycle 2UC1TL_SBR_PRC_LSP'], 'green_jobs': 0, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Karthick Jayachandran': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 2UC1TL MR'], 'green_jobs': 3, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 1UX500 Cluster'], 'green_jobs': 0, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['MRN R15.1.0 2UC1TL Cluster', 'MRN R15.1.0 2UC1TL MR', 'MRN R15.1.0 2UC1TL OPSUM', 'MRN R15.1.0 2UC1TL Without Cluster']}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 2, 'red_jobs_list': ['MRN R15.1.0 1UX500 Cluster', 'MRN R15.1.0 2UC1TL IW'], 'green_jobs': 4, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Pavan Palreddygari': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 2UC1T WITHOUT CLUSTER'], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 2, 'red_jobs_list': ['MRN R15.1.0 2UC1T WITHOUT CLUSTER', 'MRN R15.1.0 4UC1T CLUSTER'], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 4UC1T CLUSTER'], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Robin Mai': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 MRN-24x12x8x Diversity Constraint Test'], 'green_jobs': 0, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 MRN-24x12x8x Diversity Constraint Test'], 'green_jobs': 0, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Thanusha Koparthy': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 CSW Scratch Installation'], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Unni Rajanarayanan': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 1, 'red_jobs_list': ['MRN R15.1.0 8UC1T_4UC1T INTERWORKING WITH 4UC400_2UC400'], 'green_jobs': 0, 'not_executed_jobs': 2, 'not_executed_jobs_list': ['MRN R15.1.0 8UC1T_4UC1T INTERWORKING WITH 4UC400_2UC400_TEST', 'MRN R15.1.0 GreenLight with CDC config', 'WDM R15.1.0 OPSUM_TEST']}]}

Final_nested_dict_greenlight = {'Gunasekaran Loganathan': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Karthick Jayachandran': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 3, 'not_executed_jobs': 1, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 3, 'not_executed_jobs': 1, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 3, 'not_executed_jobs': 1, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 3, 'not_executed_jobs': 1, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 3, 'not_executed_jobs': 1, 'not_executed_jobs_list': []}], 'Nagarampalli Kalyan': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Pavan Palreddygari': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 2, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 1, 'red_jobs_list': ['OCS R15.1.0 Mixed CSW WDM L1 GreenLight APT'], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 1, 'red_jobs_list': ['OCS R15.1.0 Mixed CSW WDM L1 GreenLight APT'], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 2, 'red_jobs_list': ['OCS R15.1.0 Mixed CSW WDM L1 GreenLight APT', 'OCS R15.1.0 Mixed CSW WDM PSS-8 Main GreenLight APT'], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}], 'Thanusha Koparthy': [{'build_details': 'GGG28-02S 1830PSS-60.18-50', 'red_job': 1, 'red_jobs_list': ['WDM R15.1.0 GreenLight CSW Test APT_NETCONF'], 'green_jobs': 3, 'not_executed_jobs': 1, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.17-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 1, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.16-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 1, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.15-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 1, 'not_executed_jobs_list': []}, {'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 4, 'not_executed_jobs': 1, 'not_executed_jobs_list': []}], 'Unni Rajanarayanan': [{'build_details': 'GGG28-02S 1830PSS-60.13-50', 'red_job': 0, 'red_jobs_list': [], 'green_jobs': 1, 'not_executed_jobs': 0, 'not_executed_jobs_list': []}]}

#section 2
profiles_not_executed ={'Anett Rau': [{'profile': 'MRN R15.1.0 ADD6 DMAT6 D6AD2T4H - Rob Maint PrioPreempt', 'lastexecuted': 'Oct 16, 2023'}, {'profile': 'MRN R15.1.0 ADD6 DMAT6 D6AD2T4H - Rob Maint PrioPreempt - ManualTests', 'lastexecuted': 'Oct 10, 2023'}], 'Annette Opitz': [{'profile': 'TEST IR4 R15.1.0 APT CLI ANV 22.12.00', 'lastexecuted': 'Oct 09, 2023'}, {'profile': 'TEST IR4 R15.1.0 APT CLI ANV 23.12.0', 'lastexecuted': 'Oct 09, 2023'}], 'Barbara Kronmueller': [{'profile': 'MRN R15.1.0 ADD6 Alarm Test D6AD2T6', 'lastexecuted': 'Oct 10, 2023'}, {'profile': 'MRN R15.1.0 ADD6 Alarm Test DMAT6', 'lastexecuted': 'Oct 09, 2023'}], 'Florian Brenner': [{'profile': 'MRN R15.1.0 ADD6 special tests APT batch', 'lastexecuted': 'Oct 05, 2023'}], 'Gunasekaran Loganathan': [{'profile': 'WDM R15.1.0 CDC-F_2.0_CL_IRDM20-32-32L-OMDCL_AND_OT_Direct_Connected_to_MXN_ALARM', 'lastexecuted': 'Oct 10, 2023'}], 'Karthick Jayachandran': [{'profile': 'MRN R15.1.0 2UC1TL Cluster', 'lastexecuted': 'Oct 26, 2023'}, {'profile': 'MRN R15.1.0 2UC1TL MR', 'lastexecuted': 'Oct 24, 2023'}, {'profile': 'MRN R15.1.0 2UC1TL OPSUM', 'lastexecuted': 'Oct 24, 2023'}, {'profile': 'MRN R15.1.0 2UC1TL Without Cluster', 'lastexecuted': 'Oct 23, 2023'}], 'Nagarampalli Kalyan': [{'profile': 'MRN R15.1.0 Configuration of D6AD2T4H and DMAT6 in different modes and configurations', 'lastexecuted': 'Oct 24, 2023'}, {'profile': 'MRN R15.1.0 FA-TERM-Cn tunnels on D6AD2T4H and DMAT6 further tests', 'lastexecuted': 'Oct 07, 2023'}], 'Unni Rajanarayanan': [{'profile': 'MRN R15.1.0 8UC1T_4UC1T INTERWORKING WITH 4UC400_2UC400_TEST', 'lastexecuted': 'Sep 27, 2023'}, {'profile': 'WDM R15.1.0 OPSUM', 'lastexecuted': 'Oct 10, 2023'}, {'profile': 'WDM R15.1.0 OPSUM_TEST', 'lastexecuted': 'Oct 09, 2023'}]}

#section 3	 
projdict = {'Robin Mai': ['WDM R15.0.0 CSW Layer-1 Training Robin'], 'Annette Opitz': ['WDM R15.0.0 IR4 APT CLI ANV 22.12.00', 'WDM R15.0.0 IR4 APT CLI ANV 23.6.0', 'WDM R15.0.0 IR4 APT NC ANV 23.6.0']}
  	   

#exception
exception_dict = {'Others': [{'name': 'MRN R15.1.0 Distribution Hub', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 Distribution Hub', 'owner': 'Noowner', 'reason': ''}, {'name': 'R15.1.0 poll NE build url', 'owner': 'Noowner', 'reason': ''}, {'name': 'R15.1.0 poll GMRE build url', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 new GMRE Build Trigger', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 FlexOT Trigger', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 new NE build Trigger', 'owner': 'Noowner', 'reason': ''}], 'Scratch Jobs': [{'name': 'MRN R15.1.0 ADD4 LBand Scratch Installation', 'owner': 'Barbara Kronmueller', 'reason': ''}, {'name': 'MRN R15.1.0 ADD4 and Cluster Scratch Installation', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'MRN R15.1.0 ADD4 and Cluster Scratch Installation for Regression', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'MRN R15.1.0 Mixed PSS24x12x8x and Cluster Scratch Installation', 'owner': 'Noowner', 'reason': ''}, {'name': 'MRN R15.1.0 ADD6 Scratch Installation', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG Scratch Installation', 'owner': 'Noowner', 'reason': ''}], 'Hardware Profiles': [{'name': 'HW R15.1.0 ADD4 CDCMetal APT batch', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'HW R15.1.0 ADD5U 3R CDCMetal APT batch', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'HW R15.1.0 ADD5U CDCMetal APT batch', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'HW R15.1.0 MRN-24x CDCMetal APT batch', 'owner': 'Florian Brenner', 'reason': ''}, {'name': 'HW R15.1.0 WDM CDC-Diamond LSP Lifecycle S6AD600L_SFM6L_SBR', 'owner': 'Chinmay Shah', 'reason': ''}], 'Isug Testing': [{'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1205 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1300 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1304 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1310 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1400 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1408 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1410 to 1510', 'owner': 'Noowner', 'reason': ''}, {'name': 'WDM R15.1.0 ISUG UPDATE AND LSP CHECK 1500 to 1510', 'owner': 'Noowner', 'reason': ''}]}


BUILD_COMB_LIST = ['GGG28-02S 1830PSS-60.19-50', 'GGG28-02S 1830PSS-60.17-50', 'GGG28-02S 1830PSS-60.18-50', 'GGG28-02S 1830PSS-60.17-50', 'GGG28-02S 1830PSS-60.16-50', 'GGG28-02R 1830PSS-60.16-50', 'GGG28-02R 1830PSS-59.29-50', 'GGG28-02S 1830PSS-60.4-50', 'GGG28-02S 1830PSS-60.16-50', 'GGG28-02S 1830PSS-60.15-50', 'GGG28-02R 1830PSS-60.12-50', 'GGG30-01C 1830PSS-60.13-60', 'GGG30-01C 1830PSS-60.12-60', 'GGG28-02S 1830PSS-60.13-50', 'GGG28-02S 1830PSS-60.12-50']

BUILD_COMB_LIST_duplicates_removed = ['GGG28-02S 1830PSS-60.19-50', 'GGG28-02S 1830PSS-60.17-50', 'GGG28-02S 1830PSS-60.18-50', 'GGG28-02S 1830PSS-60.16-50', 'GGG28-02R 1830PSS-60.16-50', 'GGG28-02R 1830PSS-59.29-50', 'GGG28-02S 1830PSS-60.4-50', 'GGG28-02S 1830PSS-60.15-50', 'GGG28-02R 1830PSS-60.12-50', 'GGG30-01C 1830PSS-60.13-60', 'GGG30-01C 1830PSS-60.12-60', 'GGG28-02S 1830PSS-60.13-50', 'GGG28-02S 1830PSS-60.12-50']

#Section 1
#----------------------------------------------------------------------------------------------------------------------------#
env = jinja2.Environment(loader = FileSystemLoader("templates/"))
for tester in Final_nested_dict_greenlight:
    context = {"tester": tester, "buildData": Final_nested_dict_greenlight[tester], "build_details": "Greenlight Profiles"}
    template = env.get_template("portionofconsolidatedMail1.html")
    output = template.render(context)

    with open("./templates/{}_section1.html".format(tester.replace(' ','_')),"a") as fileop:
        fileop.write(output)

print("\nFinished adding data Greenlight Profiles")
time.sleep(30)


env = jinja2.Environment(loader = FileSystemLoader("templates/"))
for tester in Final_nested_dict:
    context = {"tester": tester, "buildData": Final_nested_dict[tester], "build_details": "WDM Distribution trigger"}
    template = env.get_template("portionofconsolidatedMail1.html")
    output = template.render(context)

    with open("./templates/{}_section1.html".format(tester.replace(' ','_')),"a") as fileop:
        fileop.write(output)

print("\nFinished adding data WDM Distribution trigger")
time.sleep(30)   



env = jinja2.Environment(loader = FileSystemLoader("templates/"))
for tester in Final_nested_dict_mrn:
    context = {"tester": tester, "buildData": Final_nested_dict_mrn[tester], "build_details": "MRN Distribution trigger"}
    template = env.get_template("portionofconsolidatedMail1.html")
    output = template.render(context)

    with open("./templates/{}_section1.html".format(tester.replace(' ','_')),"a") as fileop:
        fileop.write(output)

print("\nFinished adding data MRN Distribution trigger")   
time.sleep(30)



env = jinja2.Environment(loader = FileSystemLoader("templates/"))
for tester in Final_nested_dict_manual:
    context = {"tester": tester, "buildData": Final_nested_dict_manual[tester], "build_details": "Manual trigger"}
    template = env.get_template("portionofconsolidatedMail1.html")
    output = template.render(context)

    with open("./templates/{}_section1.html".format(tester.replace(' ','_')),"a") as fileop:
        fileop.write(output)

print("\nFinished adding data Manual trigger")




#----------------------------------------------------------------------------------------------------------------------------------#
#section1-sub/redjobslist 

for tester in testers:
    build_redjobs_dict = {}
    for build in range(0, len(BUILD_COMB_LIST_duplicates_removed)):
        red_jobs_list = []
        flag = False
        if BUILD_COMB_LIST_duplicates_removed[build] in BUILD_COMB_LIST:
            if tester in Final_nested_dict_greenlight and Final_nested_dict_greenlight[tester]:
                for listvalue in Final_nested_dict_greenlight[tester]:
                    if listvalue['build_details'] == BUILD_COMB_LIST_duplicates_removed[build] and listvalue['red_jobs_list']:
                        red_jobs_list += listvalue['red_jobs_list']
            if tester in Final_nested_dict and Final_nested_dict[tester]:
                for listvalue in Final_nested_dict[tester]:
                    if listvalue['build_details'] == BUILD_COMB_LIST_duplicates_removed[build] and listvalue['red_jobs_list']:
                        red_jobs_list += listvalue['red_jobs_list']
            if tester in Final_nested_dict_mrn and Final_nested_dict_mrn[tester]:
                for listvalue in Final_nested_dict_mrn[tester]:
                    if listvalue['build_details'] == BUILD_COMB_LIST_duplicates_removed[build] and listvalue['red_jobs_list']:
                        red_jobs_list += listvalue['red_jobs_list']
            if tester in Final_nested_dict_manual and Final_nested_dict_manual[tester]:
                for listvalue in Final_nested_dict_manual[tester]:
                    if listvalue['build_details'] == BUILD_COMB_LIST_duplicates_removed[build] and listvalue['red_jobs_list']:
                        red_jobs_list += listvalue['red_jobs_list']

        if red_jobs_list:
            build_redjobs_dict.update({BUILD_COMB_LIST_duplicates_removed[build] : red_jobs_list})
    
    if build_redjobs_dict:
        print("\nbuild_redjobs_dict:", build_redjobs_dict)
        #after ending of one tester

        env = jinja2.Environment(loader = FileSystemLoader("templates/")) 
        context = {"redJobsBuildDict": build_redjobs_dict}
        template = env.get_template("portion1_subRed.html")
        output = template.render(context)

        with open("./templates/{}_section1_subRed.html".format(tester.replace(' ','_')),"a") as fileop:
            fileop.write(output)

print("\nFinished adding list of all red jobs")




#-------------------------------------------------------------------------------------------------------------------------#


#section1-sub/notexecutedjobslist 

for tester in testers:
    build_notexecutedjobs_dict = {}
    for build in range(0, len(BUILD_COMB_LIST_duplicates_removed)):
        not_executed_jobs_list = []
        flag = False
        if BUILD_COMB_LIST_duplicates_removed[build] in BUILD_COMB_LIST:
            if tester in Final_nested_dict_greenlight and Final_nested_dict_greenlight[tester]:
                for listvalue in Final_nested_dict_greenlight[tester]:
                    if listvalue['build_details'] == BUILD_COMB_LIST_duplicates_removed[build] and listvalue['not_executed_jobs_list']:
                        not_executed_jobs_list += listvalue['not_executed_jobs_list']
            if tester in Final_nested_dict and Final_nested_dict[tester]:
                for listvalue in Final_nested_dict[tester]:
                    if listvalue['build_details'] == BUILD_COMB_LIST_duplicates_removed[build] and listvalue['not_executed_jobs_list']:
                        not_executed_jobs_list += listvalue['not_executed_jobs_list']
            if tester in Final_nested_dict_mrn and Final_nested_dict_mrn[tester]:
                for listvalue in Final_nested_dict_mrn[tester]:
                    if listvalue['build_details'] == BUILD_COMB_LIST_duplicates_removed[build] and listvalue['not_executed_jobs_list']:
                        not_executed_jobs_list += listvalue['not_executed_jobs_list']
            if tester in Final_nested_dict_manual and Final_nested_dict_manual[tester]:
                for listvalue in Final_nested_dict_manual[tester]:
                    if listvalue['build_details'] == BUILD_COMB_LIST_duplicates_removed[build] and listvalue['not_executed_jobs_list']:
                        not_executed_jobs_list += listvalue['not_executed_jobs_list']

        if not_executed_jobs_list:
            build_notexecutedjobs_dict.update({BUILD_COMB_LIST_duplicates_removed[build] : not_executed_jobs_list})
    
    if build_notexecutedjobs_dict:
        print("\nbuild_notexecutedjobs_dict:", build_notexecutedjobs_dict)
        #after ending of one tester

        env = jinja2.Environment(loader = FileSystemLoader("templates/")) 
        context = {"notExecutedJobsBuildDict": build_notexecutedjobs_dict}
        template = env.get_template("portion1_subNotExecuted.html")
        output = template.render(context)

        with open("./templates/{}_section1_subNotExecuted.html".format(tester.replace(' ','_')),"a") as fileop:
            fileop.write(output)

print("\nFinished adding list of all not executed jobs")




#-----------------------------------------------------------------------------------------------------------------------------------#







#section 2
if profiles_not_executed:    
    env = jinja2.Environment(loader = FileSystemLoader("templates/"))
    for tester in profiles_not_executed:
        context = {"tester": tester, "testerData": profiles_not_executed[tester], "startDate": "Oct 14th", "endDate":"Oct 20th"}
        template = env.get_template("portionofconsolidatedMail2.html")
        output = template.render(context)

        with open("./templates/{}_section2.html".format(tester.replace(' ','_')),"a") as fileop:
            fileop.write(output)

    print("\nFinished adding data for profiles not executed")
    time.sleep(30)



#section 3
if projdict:
    env = jinja2.Environment(loader = FileSystemLoader("templates/"))
    for tester in projdict:
        context = {"tester": tester, "testerData": projdict[tester], "previousRelease" : "R15.1.0"}
        template = env.get_template("portionofconsolidatedMail3.html")
        output = template.render(context)

        with open("./templates/{}_section3.html".format(tester.replace(' ','_')),"a") as fileop:
            fileop.write(output)

    print("\nFinished adding data for section 3")
    time.sleep(30)



'''
#section 4
if projdict_new:
    env = jinja2.Environment(loader = FileSystemLoader("templates/"))
    for tester in projdict:
        context = {"tester": tester, "testerData": projdict_ new[tester], "currentRelease": "R16.0.0"}
        template = env.get_template("portionofconsolidatedMail4.html")
        output = template.render(context)

        with open("./templates/{}_section3.html".format(tester.replace(' ','_')),"a") as fileop:
            fileop.write(output)

    print("\nFinished adding data for section 3")
    time.sleep(30)

'''



if exception_dict:
    env = jinja2.Environment(loader = FileSystemLoader("templates/"))
  
    context = {"exceptionData": exception_dict}
    template = env.get_template("portionofconsolidatedMail5.html")
    output = template.render(context)

    with open("./templates/exceptiontable.html","a") as fileop:
        fileop.write(output)

    print("\nFinished adding data for section 3")
    time.sleep(30)


#consolidated final data for every single tester
output = ''''''
env = jinja2.Environment(loader = FileSystemLoader("templates/"))
for tester in testers:
    context = {"tester": tester, 
        "profile_count" : 20, 
        "section1" : "{}_section1.html".format(tester.replace(' ','_')),
        "section1_redsub" :  "{}_section1_subRed.html".format(tester.replace(' ','_')),
        "section1_notexecutedsub" : "{}_section1_subNotExecuted.html".format(tester.replace(' ','_')),
        "section2" : "{}_section2.html".format(tester.replace(' ','_')), 
        "section3" : "{}_section3.html".format(tester.replace(' ','_')), 
        "section4" : "{}_section4.html".format(tester.replace(' ','_'))}
    template = env.get_template("SingleTesterPortion.html")
    output += template.render(context)

with open("./templates/all_testers_final.html","a") as fileop:
    fileop.write(output)

time.sleep(30)
print("\nFinished adding comprehensive final html")




#final comprehensive html to be sent to client
env = jinja2.Environment(loader = FileSystemLoader("templates/"))
context = {"filetoappended" : "all_testers_final.html", "exceptionFiletobeAppended": "exceptiontable.html"}
template = env.get_template("C_Mainportionofconsolidated.html")
output = template.render(context)


with open("./comprehensive_tester_data/comprehensive_final.html","a") as fileop:
    fileop.write(output)


print("\ncompleted successfully")



