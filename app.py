from flask import Flask, render_template,Response,request,redirect,url_for
from translate import Translator
import os
from PIL import Image
from pdf2image import convert_from_bytes
import pytesseract
import speech_recognition as sr
from pypdf import PdfReader 
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
app=Flask(__name__)

dic={"english":"eng","hindi":"hin","german":"ger","japanese":"jap","spanish":"spa","french":"fre","chinese":"chi","telugu":"tel"}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

@app.route('/files')
def files():
    return render_template('files.html')

@app.route('/select_text', methods=['GET','POST'])
def select():
    inp = request.form.get('Input').lower()
    out = request.form.get('Output').lower()
    input_data=request.form.get('Input_data')
    text="Invalid Inputs"
    if inp!="input language" and out!="output language":
        try:
            translator= Translator(from_lang=inp,to_lang=out)
            text = translator.translate(input_data)
        except Exception as e:
            pass
    return render_template('index.html',Input=input_data,Output=text)

def loop(init_rec,inp,out):
    s=""
    
    text=""
    while text!="quit":
        with sr.Microphone() as source:
            try:
                audio_data = init_rec.record(source, duration=3)
                text = init_rec.recognize_google(audio_data)
                print(text)
                
                translator= Translator(from_lang=inp,to_lang=out)
                text = translator.translate(text)
                print(text)
                s+=text

                return render_template('audio.html',Output=s)
            except Exception as e:
                pass

        
@app.route('/select_voice', methods=['GET','POST'])
def select_voice():
    global text
    inp = request.form.get('Input').lower()
    out = request.form.get('Output').lower()
    s=""
    
    init_rec = sr.Recognizer()
    print("Let's speak!!")
    text=""
    while text!="quit":
        loop(init_rec,inp,out)
    return render_template('audio.html',Output=s)

@app.route('/select_file', methods=['GET','POST'])
def select_file():
    inp = request.form.get('Input').lower()
    out = request.form.get('Output').lower()
    print(inp,out)
    tex=""
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            file.save(file.filename)
            reader = PdfReader(file.filename) 
            l=len(reader.pages) 
        
            for i in range(l):
                page = reader.pages[i] 
                text = page.extract_text() 
                text.strip()
                print(text)
                if inp!="input language" and out!="output language":
                    try:
                        translator= Translator(from_lang=inp,to_lang=out)
                        tex = translator.translate(text[100:450])
                    except Exception as e:
                        pass
                print(tex)
    return render_template('files.html',Output=tex)

if __name__=="__main__":
    app.run(debug=True)