import requests
import pandas as pd
import json

# Creating 2 Dataframes to store the Events and attendees Data

events_list = pd.DataFrame(columns=['Event Name', 'Event ID'])
attendees = pd.DataFrame(columns=['Event ID', 'Attendee Name'])

# Extracting the Event details using my Organisation ID(eventbrite)

source = requests.get('https://www.eventbriteapi.com/v3/organizations/826278008883/events/?token=PA62V4ALFF2R6CILOBZU')
page_content = source.content
json_obj = json.loads(page_content)
for i in json_obj['events']:
    events_list.loc[len(events_list)] = [i['name']['text'], i['id']]
# print(events_list)

# Extracting Attendee Names for each event

for i in events_list['Event ID']:
    source = requests.get(f'https://www.eventbriteapi.com/v3/events/{i}/attendees/?token=PA62V4ALFF2R6CILOBZU')
    page_content = source.content
    json_obj = json.loads(page_content)
    for j in json_obj['attendees']:
        attendees.loc[len(attendees)] = [i, j['profile']['name']]
# print(attendees)

# Merging the Dataframes to create the list of event and its attendees

df = pd.merge(events_list, attendees)
print(df)
df.to_csv('Event attendees.csv')
