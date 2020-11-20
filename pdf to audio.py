import pyttsx3
import PyPDF2

while True:
  try:
    name=input("Enter the name of the pdf")
    if name[len(name)-4::]==".pdf":
      break
    print("Invalid name entered")
  except Exception as e:
    print(e)

book = open( name, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

while True:
  try:
    pgstart=int(input("Enter the starting page number"))
    if pgstart>=1:
      break
    print("Invalid starting page entered")
  except Exception as e:
    print(e)
while True:
  try:
    pgend=int(input("Enter the ending page number"))
    if pgend>=pgstart:
      break
    print("Invalid ending page entered")
  except Exception as e:
    print(e)
while True:
  try:
    voicerate=int(input("Enter the voice rate"))
    if voicerate>=1:
      break
    print("Invalid voice rate entered")
  except Exception as e:
    print(e)

pages= pdfReader.numPages
speaker = pyttsx3.init()
for num in range(pgstart-1, pgend+1):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text,voicerate) 
    speaker.runAndWait()
