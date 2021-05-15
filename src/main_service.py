from src.chromedriver_handling import ChromeDriverHandling
from src.teams_message import TeamsMessage

import time
import os

class MainService:
    def __init__(self):
        # > Declare classes
        self.chromedriver_handling = ChromeDriverHandling()
        self.teams_message = TeamsMessage()

    
    # >
    # > Main Method
    # >
    def start_execution(self): 
        if not self.log_in():
            return False
        if not self.navigate_to_view_card():
            return False
        workers_count = self.count_workers_list()
        if not workers_count:
            return False
        else:
            if int(TeamsMessage().send_message_to_teams(workers_count)) == 200:
                return True
            else:
                return False
        
            


    # >
    # > Rules Methods
    # >
    def log_in(self):
        print(" - Log in")
        # > Web system url
        # > Test Only
        # - - - - - - -
        url_abs = os.path.abspath('repository/www/index.html')
        url_complete = 'file://' + url_abs
        # - - - - - - -
        # url = 'https://www.google.com'
        url = url_complete
        # > Navigate to web system
        if not self.chromedriver_handling.navigate_to(url):
            return False
        time.sleep(0.5)
        # > Type the email address
        if not self.chromedriver_handling.type_into('//*[@id="inputEmailAddress"]', 'email address'):
            return False
        # > Type the password
        if not self.chromedriver_handling.type_into('//*[@id="inputPassword"]', 'input password'):
            return False
        time.sleep(1)
        # > Click the login button 
        if not self.chromedriver_handling.click('//*[@href="index.html"]'):
            return False
        time.sleep(1)
        return True
       
    def navigate_to_view_card(self):
        print(" - Navigate to view card")
        # > Verify if side navigation is closed
        if self.chromedriver_handling.get_attribute('/html/body', 'class') == 'sb-nav-fixed sb-sidenav-toggled':
            # > Click the side navigation
            if not self.chromedriver_handling.click('//button[@id="sidebarToggle"]'):
                return False
        # > Verify if side navigation is open 
        if self.chromedriver_handling.get_attribute('/html/body', 'class') == 'sb-nav-fixed':
            # > Click the view card menu
            if not self.chromedriver_handling.click('//div/a[@href="tables.html"]'):
                return False
        time.sleep(1)
        return True

    def count_workers_list(self):
        print(" - Count workers list")
        # > Click the show examples
        if not self.chromedriver_handling.click('//select[@name="dataTable_length"]'):
            return False
        # > Select the 100 option
        if not self.chromedriver_handling.click('//select[@name="dataTable_length"]/option[@value="100"]'):
            return False
        # > Count all workers in the table
        workers_count = len(self.chromedriver_handling.find_elements('//tbody/tr'))
        if not workers_count:
            return False
        else:
            return workers_count