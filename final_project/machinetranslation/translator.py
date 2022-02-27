import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
'''
    This code speack with an IBM Microservice called "Language Translator" and 
    translate a text sended to this service to another language.
'''
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',  # 5.3.0 or 5.3.1
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(english_text):
    ''' Take an English text, return the translation of it into the its French version'''
    french_dictionary = language_translator.translate(
        english_text,
        model_id='en-fr').get_result()
    #print(json.dumps(french_dictionary, indent=2, ensure_ascii=False))
    french_text = french_dictionary['translations'][0]['translation']
    return french_text


def frenchToEnglish(french_text):
    ''' Take a French text, return the translation of it into the its English version'''
    english_dictionary = language_translator.translate(
        french_text,
        model_id='fr-en').get_result()
    #print(json.dumps(english_dictionary, indent=2, ensure_ascii=False))
    english_text = english_dictionary['translations'][0]['translation']
    return english_text