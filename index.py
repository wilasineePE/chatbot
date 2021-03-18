import dialogflow_v2 as dialogflow
import os
path_key = "C:\wilasinee_pj\pj\python\ggthaluangbot-a6aed6caf27a.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path_key

#*****************************************************************


project_id = "thaluangbot-lhrv"
session_id = "82d12b78-40b4-4028-a8f7-3a6a479cb2f7"
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
def detect_intent_texts(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))
    #for text in texts:
    text = texts
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text

text_re = detect_intent_texts(project_id,session_id,text,language_code)
print(text_re)






