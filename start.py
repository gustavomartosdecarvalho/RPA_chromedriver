from src.main_service import MainService
from src.log_service import LogService

import time
import os

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   
#    The following RPA is a didactic model based on real projects.
#    the robot is responsible for opening the browser, navigate the web system,
#    collecting the necessary information, closing the browser and sending a 
#    report on TEAMS 
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print("\n - - - - - - - - - - - - - - - - - - - -")
print(" - Starting workers list\n")

if MainService().start_execution():
    print(" - Extraction completed successfully")
    LogService().send_api_log(True, "Sucessfully completed")
else:
    print(" - Extraction terminated with failure")
    LogService().send_api_log(False, "Terminated with failure")

print("\n - Finish workers list")
print(" - - - - - - - - - - - - - - - - - - - -")