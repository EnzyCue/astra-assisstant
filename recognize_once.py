import azure.cognitiveservices.speech as speechsdk


#speech recognition for only recognising for 15< while not being able to stop the call unless I stop speaking.
def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription="3a28390cc8ad479897043c19d8bae3c4", region="australiaeast")
    speech_config.speech_recognition_language="en-US"

    #To recognize speech from an audio file, use `filename` instead of `use_default_microphone`:
    #audio_config = speechsdk.audio.AudioConfig(filename="YourAudioFile.wav")
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    # speech_recognition_result = speech_recognizer.recognize_once_async().get()
    speech_recognition_result = speech_recognizer.recognize_once()



    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

# recognize_from_microphone()