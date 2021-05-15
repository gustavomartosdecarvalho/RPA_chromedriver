from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

class ChromeDriverHandling:
    # > Constructor
    def __init__(self):
        self.__driver__ = self.__open_driver__()

    def __open_driver__(self):
        try:
            # > Executable path (where is the chrome driver) You can use fullpath
            executable_path = os.path.relpath('drivers/chromedriver')
            # > Download Path (where the download is placed)
            download_path = ''
            # > Set list with options for the driver
            options_list = [
                #'--headless',
                '--no-sandbox',
                '--ignore-certificate',
                '--allow-running-insecure-content',
                '--enable-features=NetworkService'
            ]
            # > Instance option list
            chrome_options = webdriver.ChromeOptions()
            # > Add options
            for op in options_list:
                chrome_options.add_argument(op)
            # > Instance Chrome driver
            driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
            # > Send Command
            driver.command_executor._commands['send_command'] = ('POST', '/session/$sessionId/chromium/send_command')
            # > Set Download Parameters
            params = {
                    'cmd': 'Page.setDownloadBehavior',
                    'params': {
                        'behavior':'allow',
                        'downloadPath': download_path
                        }
                    }
            command_result = driver.execute('send_command', params)
            # > Return the instance of the driver
            return driver
        except Exception as e:
            print(" - Error opening chromedriver: ", e)
            return None

    def close_driver(self):
        try:
            # > Close the driver instance
            self.__driver__.quit()
            return True
        except Exception as e:
            # print(" - Error to write the file {}: {}".format(file_dir, e))
            print(" - Error closing chromedriver: ", e)
            return None



    def navigate_to(self, url):
        try:
            self.__driver__.get(url)
            time.sleep(2)
            return True
        except Exception as e:
            print(" - Error opening the page : ", e)
            return False

    def get_active_url(self):
        try:
            return self.__driver__.current_url
        except Exception as e:
            print(" - Error return the url : ", e)
            return None
    
    def get_value(self, xpath):
        try:
            element = self.find_element(xpath)
            element_value = element.text
        except Exception as e:
            print(" - Error getting value : ", e)
            return False

    def get_values(self, xpath):
        try:
            data_table = []
            element_table = self.find_elements(xpath)
            for element in element_table:
                data_table.append(element.text)
            return data_table
        except Exception as e:
            print(" - Error getting values : ", e)
            return False

    def get_attribute(self, xpath, attribute):
        try:
            return str(self.find_element(xpath).get_attribute(attribute))
        except Exception as e:
            print(" - Error when clicking on the element : ", e)
            return False



    def wait_element(self, xpath, secs):
        try:
            WebDriverWait(self.__driver__, secs).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except Exception as e:
            print(" - waiting element : ", e)
            return False
    
    def find_element(self, xpath):
        try:
            if self.wait_element(xpath, 2):
                return self.__driver__.find_element_by_xpath(xpath)
            else:
                return None
        except Exception as e:
            print(" - Error find element : ", e)
            return False
    
    def find_elements(self, xpath):
        try:
            if self.wait_element(xpath, 2):
                return self.__driver__.find_elements_by_xpath(xpath)
            else:
                return None
        except Exception as e:
            print(" - Error find elements : ", e)
            return False



    def type_into(self, xpath, text):
        try:
            self.find_element(xpath).send_keys(text)
            return True
        except Exception as e:
            print(" - Typo : ", e)
            return False

    def click(self, xpath):
        try:
            self.find_element(xpath).click()
            return True
        except Exception as e:
            print(" - Error when clicking on the element : ", e)
            return False

    def move_mouse_to_element(self, xpath):
        try:
            action = ActionChains(self.__driver__)
            element_move = self.find_element(xpath)
            action.move_to_element(element_move).perform()
            return True
        except Exception as e:
            print(" - Error move to elements : ", e)
            return False

    def move_by_keyboard(self):
        try:
            action = ActionChains(self.__driver__)
            action.key_down(Keys.HOME).perform()
            time.sleep(0.1)
            action.key_down(Keys.ARROW_DOWN).perform()
            return True
        except Exception as e:
            print(" - Keyboard movement error  : ", e)
            return False


    


        


        
            






