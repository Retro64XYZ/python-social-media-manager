import yaml
import os

file_path = os.path.dirname(__file__)
if file_path != "":
    os.chdir(file_path)

with open("../config.yaml", 'r') as stream:
    try:
        configuration_file = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

twitter_consumer_key = configuration_file['twitter_consumer_key']
twitter_consumer_secret = configuration_file['twitter_consumer_secret']
twitter_access_token = configuration_file['twitter_access_token']
twitter_access_secret = configuration_file['twitter_access_secret']
