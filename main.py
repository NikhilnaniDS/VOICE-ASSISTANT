import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bangaram' in command:
                command = command.replace('bangaram', '')
                print(command)
    except:
        pass
    return command


def run_bangaram():
    command = take_command()
    print(command)
    name='Nikhil'
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'send a message in whatsapp' in command or ' in whatsapp' in command:
        talk('please give the number to send message')
        num=take_command()
        num='+91'+num
        number=''
        for i in num:
            if i!=' ':
                number+=i
        print('your number: ',number)
        talk('what message should I need to send')
        mess=take_command()
        time = datetime.datetime.now().strftime('%I:%M %p')
        time=str(time)
        if time[-2:]=='PM':
            ad=int(time[:2])+12
            time=str(ad)+time[2:]
        t1=time[:2]
        t2=time[3:5]
        try:
            pywhatkit.sendwhatmsg(num,mess,int(t1),int(t2)+1)
            talk('done boss')
        except:
            talk('something went wrong, please try again')
    elif 'how are you' in command:
        talk("I'm good, thanks for asking. How are you??")
    elif 'i am good' in command or 'good' in command:
        talk('cool')
    elif "hai" in command or 'hello' in command:
        talk('Hi, can I know ur name')
        name=take_command()
        talk('hi'+name+'how are you')
        take_command()
    elif "what is" in command:
        searchh= command.replace('what is', '')
        info = wikipedia.summary(searchh, 1)
        talk(info)
    elif 'boyfriend' in command:
        talk('Nikhil')
    elif 'who is' in command:
        searchhh=command.replace('who is','')
        info=wikipedia.summary(searchhh,1)
        talk(info)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        talk('ok bye')
        sys.exit(0)
    else:
        talk('sorry, I dont know')
        talk('Im just a beginner, im still learning')

while True:
    run_bangaram()