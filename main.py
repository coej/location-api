import json
import operator

class Activity:
    def __repr__(self):
        return repr(self.item)
    def __init__(self, deserialized_item):
        item = deserialized_item
        self.item = item
        self.confidence = item['confidence']
        self.activity_type = item['type']

class Location:
    def __repr__(self):
        return repr(self.item)
    def __init__(self, deserialized_item):
        #import operator
        item = deserialized_item
        self.item = item
        self.accuracy = item['accuracy']
        self.latitude = item['latitudeE7']
        self.longitude = item['longitudeE7']
        self.timestamp = int(item['timestampMs'])
        self.activities = []
        if 'activitys' in item:
            for a in item['activitys'][0]['activities']:
                act = Activity(a)
                self.activities.append(act)
                self.activities.sort(key=operator.attrgetter('confidence'))

fname = "C:\\Users\\chris_000\\OneDrive\\_Projects, Current\\Location data\\LocationHistory.json"

with open(fname) as jsonfile:
    data = json.load(jsonfile)
    
locs = data['locations']

loc_objs = []
for loc in locs:
    try:
        loc_obj = Location(loc)
        loc_objs.append(loc_obj)
    except ValueError as e:
        print loc
        print e.args
        continue