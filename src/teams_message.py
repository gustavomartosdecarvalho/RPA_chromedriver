import requests

class TeamsMessage:

    def send_message_to_teams(self, content):
        print(" - Send message to teams. Total workers count: ", content)
        try:
            headers = {'Content-Type': 'application/json'}
            data_input = {
                # "text": "Teams Report<br>Found "+ content['n_registros'] + " new users"
                "text": "Teams Report<br>Found "+ str(content) + " workers"
            }
            print(' - [Teams API presentation only for TEST]: ', data_input)
            # - - - - - - - - - - - -
            # > Script send to an API
            # - - - - - - - - - - - -
            # r = requests.post('TEAMS Conector', headers=headers, json=data_input, verify=False)
            # print(" - Status code: ", r.status_code)
            # return r.status_code
            return 200
        except Exception as e:
            print(" - Error send Message Teams: ", e)
            return None