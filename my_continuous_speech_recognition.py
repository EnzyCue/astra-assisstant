import azure.cognitiveservices.speech as speechsdk

"""
Explanation:
speech_recognizer is a class constructed to have all these different unique settings in the beginning. 
Then if we want to do continous speech recognition we need to be able to instantiate and connect some attributes in
our speech recognizer. This is the chunck of text in the initialise_connections(self)

When we recognise anything we immediately send it through into larity main.run on a different thread. Its better than
waiting for a que. 

A lot of it has been adapted from:
https://stackoverflow.com/questions/66833724/how-to-save-azure-continuous-speech-recognition-results-in-a-variable

"""


class MySpeechRecognizer:
    def __init__(self):
        # Establish our speech configuration settings
        speech_config = speechsdk.SpeechConfig(subscription="", region="australiaeast")
        speech_config.speech_recognition_language = "en-US"

        # Establish our audio configuration settings
        # To recognize speech from an audio file, use `filename` instead of `use_default_microphone`
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        self.initialise_connections()
        self.all_results = []
        self.query = None

        connect = speechsdk.Connection(None)

        self.new = connect.from_recognizer(self.speech_recognizer)





    # Connect callbacks to the events fired by the speech recognizer.
    def initialise_connections(self):
        # when speech is recognised, the lambda function is adjusted here to handle our newly recognised results.

        self.speech_recognizer.recognized.connect(lambda evt: self.handle_result(evt))
        self.speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
        self.speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
        self.speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
        self.speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

    # clears previous results, creates a new query that will take in all the results from the stream and starts the
    # continuous recognition.
    def start_up(self, query):
        self.clear_results()
        self.query = query




        self.speech_recognizer.start_continuous_recognition_async()



    # ends speech recognition
    def wrap_up(self):

        self.speech_recognizer.stop_continuous_recognition_async()



    # updates the current query's id and info
    def update_query(self, text, id):
        self.query.information += text.split()
        self.query.id = id

    # clears past results
    def clear_results(self):
        self.all_results = []

    # handles new results
    def handle_result(self, evt):
        print(evt.result.text)
        self.update_query(evt.result.text, evt.result.result_id)
        self.append_to_results(evt.result.text)

    # adds a piece of text into the list containing our final result
    def append_to_results(self, text):
        text = text.split()
        self.all_results = self.all_results + text


