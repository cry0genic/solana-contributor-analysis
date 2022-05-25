import json
import requests
import pandas
import matplotlib.pyplot as plt

def bubbleSort(events):
    for passnum in range(len(events)-1, 0, -1):
        for i in range(passnum):
            if ((events[i].event_date)) > ((events[i+1].event_date)):
                temp = events[i]
                events[i] = events[i+1]
                events[i+1] = temp
    return (events)

contributors = []
for i in range(13):
    res = requests.get("https://api.github.com/repos/solana-labs/solana/contributors?page={}".format(i))
    contributors+=res

with open("response.json", 'w') as f:
    json.dump(contributors, f)

f = open('response.json')

data = json.load(f)

usernames = []
for i in data:
    usernames.append(i['login'])

events = []
for username in usernames:
    resp = requests.get('https://api.github.com/users/{}/events/public'.format(username))
    resp = resp.json()

    for res in resp:
        event_id = res["id"]
        event_date = res["created_at"]
        event_date = event_date.split("T")[0]
        obj = dict()
        obj["event_id"] = event_id
        obj["event_date"] = event_date
        events.append(obj)
f.close()

with open('events.json', 'w') as f:
    json.dump(events, f)

events = bubbleSort(events)

df = pandas.DataFrame(events)
plt.scatter(df['event_date'], df['event_id'])