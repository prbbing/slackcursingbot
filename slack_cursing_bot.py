from slackclient import SlackClient
import time
import os
import random

responses_to_dan = ["Be more specific, Dan.", "Wow it is not about machine learning!", "FTAG owes you a beer always!", "Wanna eat some pasta?", "I run out of bread, do you have some?", "Dan you speak too much!"]



token = os.environ.get('BINGBOT_Token')
slack_client = SlackClient(token)

if slack_client.rtm_connect():
    while True:
        events = slack_client.rtm_read()
        for event in events:
            print event
            if (
                'channel' in event and
                'text' in event# and
                #event.get('type') == 'message'
            ):
                channel = event['channel']
                text = event['text']
                print text
                if 'CDS' in text and 'asses' not in text:
                    slack_client.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text="Fuck CDS, it is appalling. People who post comments on CDS never get wet while their asses are being eaten!",
                        as_user='true:'
                    )
            if (
                'channel' in event and
                'text' in event and
                'user' in event
            ):
                user = event['user']
                if "USLACKBOT" in user: 
                    slack_client.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text="Slackbot you are lame!",
                        as_user='true:'
                    )
            if (
                'channel' in event and
                'text' in event and
                'user' in event
            ):
                user = event['user']
                if "U0KDQGKN1" in user:
                    item = int(random.randrange(0, 5))
                    slack_client.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text=responses_to_dan[item],
                        as_user='true:'
                    )
        time.sleep(1)
else:
    print('Connection failed, invalid token?')



