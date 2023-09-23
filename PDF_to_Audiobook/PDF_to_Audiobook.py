# this project is about to convert the pdf into an audiobook

import pyttsx3
# py means python, t = text, t= two, s =speach, x3 = version
import PyPDF2 # this library allows you to interact with pdf and python

book = open('proof.pdf', 'rb') # means that you are going to make it readable for a computer
pdfReader = PyPDF2.PdfFileReader(book) # means that you are going to use the function PdfFileReader to read the pdf


#pages = pdfReader.numPages # this makes you the number of pages
#print(pages) # print the number of pages
 
speaker = pyttsx3.init() # means that we are going to inicializate the library
voices = speaker.getProperty('voices') # to change the voice of the speaker
speaker.setProperty('voice', voices[0].id) # this change the voice of the speker for an english man voice, becaise it has the id[0] but if you want it in spanish then use the id[14] or id[15]

page = pdfReader.getPage(7) # the number of page that you want to read, but remmeber that in programming we start with 0 meaining the first page
text = page.extractText() # this is to convert the page extracted into a readable text for humans
#speaker.say('Look mama I can talk') # here put the speach to say
speaker.say(text)
speaker.runAndWait() # put to talk the library

# if you need to read especific part on the text in a range of pages use this command below
"""
for num in range(7,pages): # pages means the length of pages = pdfReader.numPages 
    # here is going to read from the 7 page until the lenght of the pages means the whole pdf
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
"""