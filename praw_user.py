import praw
from praw_object_data import retry_if_broken_connection

client_id = "GULq9J_pOyi4iA"
secret="ViIRIj82a08aJzkNBMeOsG3noOg"
username='Clairelovesgrapefrui'
password='Zzl@19930117reddit'
user_agent = 'tree grabber for reddit, made by /u/antirabit, run by someone else'

@retry_if_broken_connection
def scraper():
    r = praw.Reddit(client_id=client_id,
                    client_secret=secret,
                    username=username,
                    password=password,
                    user_agent=user_agent)
    return r


    
