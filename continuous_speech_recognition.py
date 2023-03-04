import azure.cognitiveservices.speech as speechsdk
import time
"""Explanation:
speech_recognizer is a class constructed to have all these different unique setting in the beginning. 
Then if we want to do continous speech recognition we need to be able to instantiate and connect some attributes in
our speech recognizer. This is the chunck of text with the .connect

https://stackoverflow.com/questions/66833724/how-to-save-azure-continuous-speech-recognition-results-in-a-variable

problems with code: 
- no way of stopping it, also no way of stopping it from ignition.py
- no way of extracting the text that we're receiving directly
-  code is super ugly man


"""

def speech_recognize_continuous_from_file():


    speech_config = speechsdk.SpeechConfig(subscription="3a28390cc8ad479897043c19d8bae3c4", region="australiaeast")
    speech_config.speech_recognition_language = "en-US"

    # To recognize speech from an audio file, use `filename` instead of `use_default_microphone`:
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")

    done = False

    # def stop_cb(evt):
    #     """callback that signals to stop continuous recognition upon receiving an event `evt`"""
    #     print('CLOSING on {}'.format(evt))
    #     nonlocal done
    #     done = True

    all_results = []

    def handle_final_result(evt):
        all_results.append(evt.result.information)

    speech_recognizer.recognized.connect(handle_final_result)
    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.1)

    speech_recognizer.stop_continuous_recognition()


speech_recognize_continuous_from_file()