from colorama import Fore, Style
from dotenv import load_dotenv
import json
import ldclient
from ldclient.config import Config
from ldclient.versioned_data_kind import FEATURES
import os
import time
from utils.create_context import *
from utils.apiHandler import checkRateLimit as api_call

'''
Get environment variables
'''
load_dotenv()

SDK_LIST = json.loads(os.environ.get('SDK_LIST'))

'''
Evaluate all flags in an environment
'''
def evaluate_all_flags(context):
    # Method to get all flags from the feature store. Taken from https://github.com/launchdarkly/python-server-sdk/blob/d152455b89cb70164d8487a1cc0b47f92017a5c4/ldclient/client.py#L549
    feature_store = ldclient.__client._store.all(FEATURES, lambda x: x)
    for key in feature_store.keys():
        result = ldclient.get().variation(key, context, False)

'''
Main loop to evaluate flags across multiple environments
'''
def evaluate_flags(environments):
    context = create_multi_context()
    for env in environments:
        print(Fore.CYAN + f'*** Evaluating environment: sdk-****-{env[-4:]} ***')
        print(Style.RESET_ALL)
        ldclient.set_config(Config(env))
        if not ldclient.get().is_initialized():
            print("*** SDK failed to initialize. Please check your internet connection and SDK credential for any typo.")
            exit()
        evaluate_all_flags(context)
        time.sleep(1)
        ldclient.get().flush()
        time.sleep(1)
        ldclient.get().close()
        time.sleep(10)
        

def run_multi_eval():
    while True:
        try:
            evaluate_flags(SDK_LIST)
        except Exception as e:
            print(f'Error: {e}')
            break