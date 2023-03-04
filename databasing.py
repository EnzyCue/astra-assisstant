import sqlite3
from datetime_to_unixepoch import datetime_to_unixepoch

"""Manages communication with the database."""


# returns the number for the last episode.
def get_last_episode_number(cursor):
    cursor.execute("SELECT * FROM events ORDER BY episode DESC LIMIT 1;")

    episode_number = cursor.fetchone()[1]

    return episode_number


# adds a single event into the database.
def add_event(event, event_sequence, episode_number, cursor):

    # the event's time of creation is converted into unixepoch-time to turn it into an integer
    time = datetime_to_unixepoch(event.time_of_creation)

    # event's information is converted from a list of strings into a single string with spaces for storage requirements.
    info = " ".join(event.information)

    cursor.execute("""INSERT INTO events (
                                        episode, sequence, 
                                        time, type, 
                                        information
                                        ) 
                                        VALUES (?, ?, ?, ?, ?)""",
                   (
                       episode_number, event_sequence,
                       time, event.type,
                       info
                   )
                   )
    return


# adds a whole episode into the database.
def add_episode(episode, cursor):
    # the current episode number should be 1 + the last episode number.
    episode_number = get_last_episode_number(cursor) + 1

    for i in range(0, episode.no_of_events):
        add_event(event=episode.list_of_events[i], event_sequence=i, episode_number=episode_number, cursor=cursor)

    return


# first function an episode is sent to for being uploaded into the database.
def upload_episode(episode):
    connection = sqlite3.connect('event_logs.db')

    cursor = connection.cursor()

    add_episode(episode, cursor)

    connection.commit()

    connection.close()
    return


# if __name__ == '__main__':
#     connection = sqlite3.connect('event_logs.db')
#
#     cursor = connection.cursor()
#
#     cursor.execute("""CREATE TABLE IF NOT EXISTS events (
#                     id integer primary key,
#                     episode int,
#                     sequence int,
#                     time int,
#                     type int,
#                     information string
#                     )""")
#
#     connection.commit()
#     connection.close()
