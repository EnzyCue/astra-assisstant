from datetime import datetime
from constants import QUERY_TYPE, REPLY_TYPE, ACTION_TYPE
import databasing


"""
Classes with the goal of keeping track of queries, help with immediate speech to text errors and manages the 
immediate working memory before the episode is eventually sent off into the database and wiped clean.
"""


# query class, containing text for a query, its id, time of creation?
class Event:
    def __init__(self, text, id):
        self.information = text
        self.id = id
        self.time_of_creation = datetime.utcnow()
        self.type = None


class Query(Event):
    def __init__(self, text, id):
        Event.__init__(self,text, id)
        self.type = QUERY_TYPE


class Reply(Event):
    def __init__(self):
        Event.__init__(self, text, id)
        self.type = REPLY_TYPE


class Action(Event):
    def __init__(self):
        Event.__init__(self, text, id)
        self.type = ACTION_TYPE


# Contains the events for an episode. The specific attributes are intended to be useful to the main program.
# perhaps it could be organised better, but I like the look of this, I feel it makes a lot of sense.
class LarityEpisode:
    def __init__(self):
        # for all "query" type events in this episode:
        self.list_of_queries = []
        self.latest_query = None
        self.no_of_queries = 0

        # for all "reply" type events in this episode:
        self.list_of_replies = []
        self.latest_reply = None
        self.no_of_replies = 0

        # for all "action" type events in this episode:
        self.list_of_actions = []
        self.latest_action = None
        self.no_of_actions = 0

        # a list of the different event objects in the sequence they were implemented this episode.
        self.list_of_events = []
        self.latest_event = None
        self.no_of_events = 0

        self.is_active = False

    def add_query(self, query):
        self.list_of_queries.append(query)
        self.no_of_queries += 1
        self.latest_query = query
        self.add_event(query)

    def add_action(self, action):
        self.list_of_actions.append(action)
        self.no_of_actions += 1
        self.latest_action = action
        self.add_event(action)

    def add_reply(self, reply):
        self.list_of_replies.append(reply)
        self.no_of_replies += 1
        self.latest_reply = reply
        self.add_event(reply)

    def add_event(self, event):
        self.list_of_events.append(event)
        self.latest_event = event
        self.no_of_events += 1

    # uploads data before clearing episode
    def end(self):
        self.upload()
        self.__init__()

    # uploads data to the sqlite .db file.
    def upload(self):
        databasing.upload_episode(self)