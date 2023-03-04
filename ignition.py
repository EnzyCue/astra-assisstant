from datetime import datetime

import query_manager
from constants import NUMBER_OF_MINUTES
from main import run
from my_continuous_speech_recognition import MySpeechRecognizer
from time_difference import getDuration
import threading
#from multiprocessing import Process


"""
A function that is constantly running in the background of my computer waiting for an input of 0 (this can later be automated using
different methods like authotkey). Once it receives that it starts to listen and print out any words recognised, makes saves of it and sends it to our
main program where classification and analysis can be directed to occur.
"""


"""
whats left: 
- concurency implenation: implement multithreading for the disconnection with azure, to connect a new one. 

- 
- add certain keyinput for soft reset (automatic recursion).  Not possible unless we implement concurrency. 


- send live texts to main, meaning that even if the push-to-talk is ongoing. Send recognised results when a pause is taken.
this will also decrease latency for you letting go of the button.


- add certain keyinput disregard last sentence keyinput. 


"""


# responsible for using azure to recognise speech until the push to talk ends
def recognise(recogniser, episode):

    #query = start_recognition(recogniser, episode)
    start_recognition(recogniser, episode)

    # while recognising we want to listen for when the person wants it cancelled.
    while True:
        newpassword = input("")
        if newpassword == "0":


            # x = threading.Thread(target=stop_recognition, args=(recogniser, episode, query,))
            # x.start()
            stop_recognition(recogniser, episode)
            run(episode)


            break
    return


# creates multiple objects to ready things for recognition
def start_recognition(recogniser, episode):

    # create a new query, send it to the speech recognition platform and add it to the episode.
    query = query_manager.Query(text=[], id=None)
    recogniser.start_up(query)
    episode.add_query(query)

    episode.is_active = True

    return query


# ends recognition and sends the results
def stop_recognition(recogniser, episode, query):

    # send the specific query as well as the entire event to main.py


    # stop the speech recognising.
    del recogniser





    return


# a recursive function that is always running as long as the PC is on
def recursive_stream(recogniser, episode):
    # filter to start the speech recognition
    password = input("\nEnter password: ")

    if password == "0":

        """if the episode is not a new one, lets check how long has it been since it was last used it to see if we 
        should upload it to the database and create a new sqlite file. """

        if episode.is_active and getDuration(episode.latest_query.time_of_creation, datetime.utcnow(),
                                             interval='minutes') >= NUMBER_OF_MINUTES:

            # puts data into a database and wipes the episode.
            episode.end()

            recognise(recogniser, episode)

        else:
            recognise(recogniser, episode)

    return recursive_stream(recogniser, episode)


if __name__ == '__main__':
    # creates the speech recognition object outside the recursive function oherwise we'll eventually get stack overflow
    speech_recogniser = MySpeechRecognizer()

    # Larity episode initialisation
    larity_episode = query_manager.LarityEpisode()

    # recursive_stream(speech_recogniser, larity_episode)
    recursive_stream(speech_recogniser, larity_episode)
