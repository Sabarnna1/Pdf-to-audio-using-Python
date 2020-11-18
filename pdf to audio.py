# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:05:53 2020

@author: SABARNNA SEN
"""

import pyttsx3
import PyPDF2
name=input("Enter the name of the pdf")
book = open( name, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pgstart=int(input("Enter the starting page number"))
pgend=int(input("Enter the ending page number"))
pages= pdfReader.numPages
speaker = pyttsx3.init()
for num in range(pgstart-1, pgend+1):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text) 
    speaker.runAndWait()