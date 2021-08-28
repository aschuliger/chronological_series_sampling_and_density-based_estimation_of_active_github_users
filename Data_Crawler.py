import requests
import config
import json

class Data_Crawler:
    def __init__(self, validation):

        # There are three personal tokens in the config file, so here, we simply figure out which one is necessary depending on the parameter
        self.token = config.access_token # Normal token
        if validation == 0: # First interval validation token
            self.token = config.access_token_validation
        elif validation == 1: # Second interval validation token
            self.token = config.access_token_validation_2
        self.rate_limit = 60
        self.max_responses = 30
        self.headers ={
            'Authorization': 'token '+ self.token,
        }

    #sample NUM ids since UID    
    def sample(self, uid):
        response = requests.get('https://api.github.com/users?since='+str(uid),headers=self.headers)
        sample_data = response.json()
        return sample_data

    # Calculates the length of a given interval
    def extract_length(self, sample_data):
        return sample_data[29]['id'] - sample_data[0]['id'] + 1

    # Calculates the number of responses in a given interval
    def extract_number_of_response(self, sample_data):
        return len(sample_data)

    # Calculates what the next interval will be
    def calculate_next_interval(self, last_value, c):
        return last_value + c

    #use downloaded data to build estimator  
    def estimate(self, densities, interval_count, maximum):
        estimation = (maximum/interval_count)*(densities)
        return estimation