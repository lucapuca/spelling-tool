import random
import sys
import speech_recognition as sr
import pyttsx3

def speak(text):
    """Speaks the given text using pyttsx3."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to the microphone and returns the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please spell the word.")
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
            text = r.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def main():
    words_file = "words.txt"
    try:
        with open(words_file, "r") as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {words_file} not found.")
        return

    if not words:
        print("Error: No words found in the file.")
        return

    # 1. Pick a random word
    target_word = random.choice(words)
    
    # 2. Read out loud the word
    # print(f"Please spell: {target_word}") # Removed to avoid cheating
    
    speak(f"Please spell the word {target_word}")

    # 3. Listen to the spelling
    user_input = listen()

    if user_input is None:
        speak("I didn't hear anything. Exiting.")
        sys.exit(0)

    print(f"You said: {user_input}")

    # Normalize input and target
    # User might say "C A T" (with spaces) or "cat"
    # We remove spaces and convert to lower case
    normalized_input = user_input.replace(" ", "").lower()
    normalized_target = target_word.lower()

    # 4. Output correct/wrong
    if normalized_input == normalized_target:
        print("Output: Correct")
        speak("Correct")
    else:
        print("Output: Wrong")
        speak("Wrong")
        
        # If wrong says/writes the right spelling
        spelled_out = ", ".join(list(target_word))
        print(f"The correct spelling is: {target_word}")
        speak(f"The correct spelling is {spelled_out}")

    # Exit
    sys.exit(0)

if __name__ == "__main__":
    main()
