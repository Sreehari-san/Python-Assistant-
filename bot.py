import datetime
import wikipedia
import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 145)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("AI ON") # Print when bot is ON
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'something' in command:
                command = command.replace('something', '')
                print("Command")
    except:
        pass
    return command

  # loki is bot name you can edit it, if you edit function name, you must change name in last line 'run_loki()' :)
  
def run_loki():
    command = take_command()
    print(command)
    
    #commands
    
    if 'hai' in command:
        talk("Hai there")

    elif 'hello' in command:
        talk("Hello i am <NAME>")

    elif 'youtube' in command:
        song = command.replace('youtube', '')
        talk('Playing' + song + ' in Youtube')
        pywhatkit.playonyt('Playing' + song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I %M %p")
        print(time)
        talk("Current time is" + time)

    elif 'wiki' in command:
        search = command.replace('wiki', '')
        info = wikipedia.summary(search, 1)
        talk("Results found about" + search)
        print(info)
        talk(info)

    elif 'date' in command:
        date = datetime.datetime.today().strftime("%Y-%M-%D")
        print(date)
        talk("today is " + date)

    elif 'my name' in command:
        talk("Oh sorry! i don't know your name")
        name = input("Enter your name here: ")
        talk("Ok " + name)

    elif 'search' in command:
        app = command.replace("search", '')
        talk("Search result of " + app)
        url = "https://www.google.com/search?q="
        brows = url+app
        webbrowser.open(brows)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H-%M %p")
        print(time)
        talk(time)

    elif 'love you' in command:
        print("\nSorry\n")
        talk("I have a relationship with wifi")

    elif 'wish me happy birthday' in command:
        talk("Your name please")
        name = input("User: ")
        talk("Happy birthday " + name)
        thank = input(name + ": ")

        if thank == "thanks":
            print("\nno need of thanks\n")
            talk("no need of thanks")

    elif 'open' in command:
        app = command.replace("open", "")
        talk("Opening " + app)
        url = "https://www.google.com/search?q="
        openApp = url+app
        webbrowser.open(openApp)

    elif command == 'info':
        talk("I am loki ai system version one")

    elif 'code editor' in command:
        print("\nMy IDE: pycharm\nLanguage: python\n")
        talk("I am made python and my ide is pycharm")
        url = "https://www.google.com/search?q="
        result = url+command
        webbrowser.open(result)

    elif 'your place' in command:
        print("\nI am from India, Kerala\n")
        talk("I am from India Kerala")

    elif 'your creator' in command:
        print("\nSreehari\n")
        talk("My creator is Sreehari")

    elif command == 'how are you':
        print("\nFine\n")
        talk("I am fine")

    elif command == 'good morning':
        print("\nOoh good morning\n")
        talk("good morning")

    elif command == 'good afternoon':
        print("\ngood afternoon\n")
        talk("good afternoon")

    elif command == 'good evening':
        print("\nGood evening\n")
        talk("good evening")

    elif command == 'good night':
        print("\nGood night\n")
        talk("good night sweet dreams")

    elif 'your name' in command:
        print("\nLoki\n")
        talk("my name is loki")

    elif 'contact creator' in command:
        print("\nig: its.me_jack_ser\n")
        talk("message him on instagram")

    elif 'jokes' in command:
        print("\nHello\n")

    elif 'loki you girl' in command:
        print("\nNo\n")
        talk("No i am a bot")

    elif 'you a boy' in command:
        print("\nNo\n")
        talk("I am a bot")

    elif 'bye' in command:
        while True:
            import time

            talk("turning off")
            time.sleep(1)
            exit()


    elif command == 'exit':
        while True:
            import time
            talk("turning off")
            time.sleep(0.5)
            exit()

    elif 'are you a singer' in command:
        print('Some time')
        talk("I can sing")
        print("Youtube <Song name> it will open youtube and you can hear your song")

    elif 'Do you know maths' in command:
        print("Yes of course i know")
        talk("yes i know maths")
        talk("In version one only addition subtraction and multiplication available")

        # make a random password
        
    elif 'password generator' in command:
        import time
        import random

        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "0123456789"

        mix = lower + upper + nums
        length = 9
        password = "".join(random.sample(mix, length))
        print("1 minute")
        talk("your password is generating")
        time.sleep(2)
        print('Password is: "' + password + '"')
        talk("Your password is here")

        
    elif 'you can do' in command:
        import time

        print("Many things")
        talk("I can chat with you sing song and many thing")
        time.sleep(0.05)
        talk("In version 2 game option translate and much more options will available")

    elif 'help me in homework' in command:
        print("say 'search <Your search>' or for search in wikipedia say 'wiki <your search>'")
        talk("say search or for search in wikipedia say wiki")
  
        # you can add command in your own
        # if there is no command like that
        
    else:
        print("I did not understand")
        talk("sorry i did not understand")

while True:
    run_loki()
