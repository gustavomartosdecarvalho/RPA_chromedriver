from datetime import datetime
import requests

class LogService:

    def send_api_log(self, log_success, log_message):
        print(" - Send Log: {}   - Status: {}".format(log_message, log_success))
        try:
            timestamp_now = datetime.now().timestamp()
            header = {"Content-Type":"application/json"}
            data_input = {
                "application": "RPA",
                "service": "workers_list",
                "datalog": timestamp_now,
                "sucess": log_success,
                "mess": log_message
            }
            print(' - [Log API presentation only for TEST]: ', data_input)
            # - - - - - - - - - - - -
            # > Script send to an API
            # - - - - - - - - - - - -
            # address = "http://xxx"
            # r = requests.post(address, header = header, json = data_input, verify = False)
            # if int(r.status_code) == 200:
            #     print(" - Log sent successfully")
            #     return True
            # else:
            #     print(" - Failed to send log")
            #     return False
        except Exception as e:
            print(" - Error to send log: ", e)
            return False

