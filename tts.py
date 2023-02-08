import PyPDF2 
import textract

from gtts import gTTS
# play the converted audio
import os

filename = 'HS.pdf' 

#open allows you to read the file.

FObj = open(filename,'rb')

#The pdfReader variable is a readable object that will be parsed.

pr = PyPDF2.PdfReader(FObj)

# number of pages will allow us to parse through all the pages.

num_pages = 5
count = 3
mytext = ""

#The while loop will read each page.
while count < num_pages:
    pageObj = pr.pages[count]
    count +=1
    mytext += pageObj.extract_text()

if mytext != "":
   mytext = mytext  
#convert scanned/image based PDF files into text.
else:
   mytext = textract.process("HS.pdf", method='tesseract', language='eng')  

t=" ".join(mytext.split())
print(t)

#text to speech
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 

myobj = gTTS(text=t, lang=language)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("HideandSeek.mp3")
  
# Playing the converted file
os.system("HideandSeek.mp3")