#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyaudio
import re
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from datetime import date
from pyowm import OWM
from time import strftime
import urllib.request as urllib2
from bs4 import BeautifulSoup as soup


# In[3]:



#news for today topic

news_url="https://news.google.com/news/rss"
Client=urllib2.urlopen(news_url)
xml_page=Client.read()
Client.close()
soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
for news in news_list[:5]:
    print(news.title.text.encode('utf-8'))
    
                
       


# In[4]:


# current weather topic
city = "Chennai"
owm = OWM(API_key='c7407f62b06f71620683b4699c66821f')
obs = owm.weather_at_place(city)
w = obs.get_weather()
k = w.get_status()
x = w.get_temperature(unit='celsius')
print('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))


# In[8]:


# web browser registering
import webbrowser
url = "youtube.com"
url2 ="gitup.com"
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register("msedge",None,webbrowser.BackgroundBrowser(edge_path))
#webbrowser.get("msedge").open_new_tab(url2)


# In[14]:


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
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    
    elif 'thank You' in command:
        print("Your Welcome")
        talk("Your Welcome")
        
    elif 'time please' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
        
    elif 'news for today' in command:
         for news in news_list[:5]:
                
                print(news.title.text.encode('utf-8'))
           
        
    
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    elif 'date please' in command:
        today = date.today()
        print(today)
        talk(today)
        
    elif 'open google' in command:
        talk("opening google")
        webbrowser.open("google.com")
        
    elif 'bye' in command:
         exit(0)
            
    elif 'open github' in command:
        talk("opening github")
        webbrowser.open("github.com")
        
    elif 'local disk c' in command:
        talk("opening local disk C")
        webbrowser.open("C://")
        
    elif 'local disk F' in command:
        talk("opening local disk F")
        webbrowser.open("F://")
        
    elif 'local disk E' in command:
        talk("opening local disk E")
        webbrowser.open("E://")
        
    elif 'open youtube' in command:
        talk("opening youtube")
        webbrowser.open("youtube.com")
        
    elif 'open spotify' in command:
        talk("opening spotify")
        webbrowser.open("spotify.com")
        
    elif 'open whatsapp' in command:
        talk("opening whatsapp")
        webbrowser.open("whatsapp.com")
        
    elif 'current weather' in command:
        print('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
        talk('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
    
    elif 'who are you' in command:
        print("I am Alexa vitual voice assistant developed by Mohana Priya")
        talk("I am Alexa vitual voice assistant developed by Mohana Priya")
    
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            print('Hello My Dear Friend. Good morning')
            talk('Hello My Dear Friend. Good morning')
        elif 12 <= day_time < 18:
            print('Hello My Dear Friend. Good afternoon')
            talk('Hello My Dear Friend. Good afternoon')
        else:
            print('Hello My Dear Friend. Good evening')
            talk('Hello My Dear Friend. Good evening')
        
    elif 'are you single' in command:
            print('I am in a relationship with wifi')
            talk('I am in a relationship with wifi')
        
    elif 'tell me about' in command:
        reg_ex = re.search('tell me about (.*)', command)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)
                print(ny.content[:100].encode('utf-8'))
                talk(ny.content[:100].encode('utf-8'))
        except Exception as e:
                print(e)
                talk(e)
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    else:
        print('Please say the command again.')
        talk('Please say the command again.')


while True:
    run_alexa()


# In[ ]:





# In[ ]:





# In[ ]:




