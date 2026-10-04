import speech_recognition as sr
import pyttsx3

# Create speech recognizer
recognizer = sr.Recognizer()

# Create text-to-speech engine
engine = pyttsx3.init()

# Predefined questions and answers
questions = {
    "what is python":
        "Python is a high level programming language.",

    "what is artificial intelligence":
        "Artificial intelligence is a technology that enables machines to perform intelligent tasks.",

    "what is machine learning":
        "Machine learning allows computers to learn from data.",

    "what is nlp":
        "NLP stands for Natural Language Processing.",

    "what is speech recognition":
        "Speech recognition converts spoken language into text.",

    "what is text to speech":
        "Text to speech converts written text into spoken audio."
}


print("VOICE QUESTION ANSWERING SYSTEM")
print("--------------------------------")

try:

    # Open microphone
    with sr.Microphone() as source:

        print("Adjusting microphone...")
        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        print("Ask your question...")

        # Record voice
        audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=10
        )

    print("Processing...")

    # Convert speech into text
    question = recognizer.recognize_google(audio)

    # Convert to lowercase
    question = question.lower()

    # Remove punctuation
    for symbol in ".,!?;:":
        question = question.replace(symbol, "")

    print("\nYour Question:")
    print(question)

    # Find answer
    answer = questions.get(
        question,
        "Sorry, I do not know the answer."
    )

    # Display answer
    print("\nAnswer:")
    print(answer)

    # Speak the answer
    engine.say(answer)
    engine.runAndWait()


except sr.WaitTimeoutError:

    print("\nNo question was detected.")


except sr.UnknownValueError:

    print("\nSorry, I could not understand your question.")


except sr.RequestError:

    print("\nSpeech recognition service is unavailable.")


except OSError:

    print("\nMicrophone was not found.")