from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToSpanish")
def englishToSpanish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_translation = machinetranslation.translator.englishToFrench(textToTranslate)
    return french_translation

@app.route("/spanishToEnglish")
def spanishToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_translation = machinetranslation.translator.frenchToEnglish(textToTranslate)
    return english_translation

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
