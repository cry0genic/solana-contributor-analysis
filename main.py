import json
import requests
# import pandas
# import matplotlib.pyplot as plt

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

# df = pandas.DataFrame(events)
# df = df.sort(['event_date'])

# plt.scatter(df['event_date'], df['event_id'])