import dialogflow_v2 as dialogflow
import os
credential_path = "C:\/non\good-doc-eqee-1ec9403d234b.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
project_id = "good-doc-eqee"
session_id = "284614b9-f843-4c01-b1c2-61702b4195ee"
language_code = "Thai-th"
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import json

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

text = input("let's text ")
text_re = detect_intent_texts(project_id, session_id, text, language_code)
print(text_re)