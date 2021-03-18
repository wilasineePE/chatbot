import dialogflow_v2 as dialogflow
import os
path_key = "C:\wilasinee_pj\pj\python\ggthaluangbot-a6aed6caf27a.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path_key

#*****************************************************************


project_id = "thaluangbot-lhrv"
sesseion_id = "82d12b78-40b4-4028-a8f7-3a6a479cb2f7"
language_code = "Thai-th"

 #****************************************************************

from flask import Flask ,request,abort
from linebot import(
    LineBotApi , WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)
from linebot.models import * 
import json

#**************************************
text = input("let's text : ")

app = Flask(__name__)
def detect_intents_texts(project_id,sesseion_id,texts,language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id,sesseion_id)
    print('session_path : {}\n'.format(session))

    text = texts
    text_input = dialogflow.types.TextInput(text=text,language_code=language_code)
    query_input = dialogflow.types.QueryInput(text = text_input)
    response = session_client.detect_intent(session= session,query_input =  query_input)
    return response.query_result.fulfillment_text

text_re = detect_intents_texts(project_id,sesseion_id,text,language_code)
print(text_re)






