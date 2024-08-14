from tokenize import String
from gtts import gTTS
import pandas as pd
from googletrans import Translator


def translate_hindi_to_english(hindi_text):
    # Create a Translator object
    translator = Translator()

    # Translate the Hindi text to English
    translated = translator.translate(hindi_text, src='hi', dest='en')
    
    # Get the translated text
    english_text = translated.text
    return english_text

excelFile=pd.read_excel("source.xlsx")
print(excelFile)
for index, item in excelFile.iterrows():
    # Your text in Hindi
    text = item['Information']

    english_text = translate_hindi_to_english(text)

    # Creating an object of gTTS class with the text and language as Hindi
    tts = gTTS(text=text, lang='hi')
    no=str(item['No'])
    name=item['Name']
    # Saving the converted audio in an mp3 file
    tts.save(no+"H"+name+".mp3")

    print("Hindi text has been converted to",name,"Hindi.mp3")

    tts = gTTS(text=english_text, lang='en')

    # Saving the converted audio in an mp3 file
    tts.save(no+"E"+name+".mp3")

    print("English text has been converted to",name,"English.mp3")

    