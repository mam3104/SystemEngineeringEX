#-*- coding: utf-8 -*-

from __future__ import print_function
import random

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            #'title': "SessionSpeechlet - " + title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_speechlet_response_launch(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
         "directives": [
            {
                "type": "Display.RenderTemplate",
                "template": {
                    "type": "ListTemplate1",
                    "token": "List",
                    "backButton": "VISIBLE",
                    "backgroundImage": {
                        "contentDescription": "背景",
                        "sources": [
                            {
                                "url": "https://mam3104.com/static/image/qol/bg1.png"
                            }
                        ]
                    },
                    #"title": "スキルリスト",
                    "listItems": [
                        {
                            "token": "list1",
                            "textContent": {
                                "primaryText": {
                                    "type": "PlainText",
                                    "text": "スコアを表示"
                                }
                            }
                        },
                        {
                            "token": "list2",
                            "textContent": {
                                "primaryText": {
                                    "type": "PlainText",
                                    "text": "ランキングを表示"
                                }
                            }
                        },
                        {
                            "token": "list3",
                            "textContent": {
                                "primaryText": {
                                    "type": "PlainText",
                                    "text": "ミニゲーム"
                                }
                            }
                        },
                        {
                            "token": "list4",
                            "textContent": {
                                "primaryText": {
                                    "type": "PlainText",
                                    "text": "終了"
                                }
                            }
                        }
                    ]
                }
            }
        ],
        'shouldEndSession': should_end_session
    }

def build_speechlet_response_image1(title, output, reprompt_text, should_end_session):
    rand = random.randrange(1, 4)
    if rand == 1:
        URL = "https://mam3104.com/static/image/qol/VerL/0.png"
    elif rand == 2:
        URL = "https://mam3104.com/static/image/qol/VerL/1.png"
    elif rand == 3:
        URL = "https://mam3104.com/static/image/qol/VerL/2-1.png"
    elif rand == 4:
        URL = "https://mam3104.com/static/image/qol/VerL/2-2.png"
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Standard',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
         "directives": [
            {
                "type": "Display.RenderTemplate",
                "template": {
                    "type": "BodyTemplate7",
                    "token": "SampleTemplate_3476",
                    "backButton": "VISIBLE",
                    #"title": "今日の活動時間：8時間21分",
                    "backgroundImage": {
                        "contentDescription": "背景",
                        "sources": [
                            {
                                "url": "https://mam3104.com/static/image/qol/VerL/0-B.jpg"
                            }
                        ]
                    },
                    "image": {
                        "contentDescription": "染色体-胎児",
                        "sources": [
                            {
                                "url": URL
                            }
                        ]
                    }
                }
            }
        ],
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_image2(title, output, reprompt_text, should_end_session):
    rand = random.randrange(1, 3)
    if rand == 1:
        URL = "https://mam3104.com/static/image/qol/VerL/3.png"
    elif rand == 2:
        URL = "https://mam3104.com/static/image/qol/VerL/3-EX.png"
    elif rand == 3:
        URL = "https://mam3104.com/static/image/qol/VerL/4.png"
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Standard',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
         "directives": [
            {
                "type": "Display.RenderTemplate",
                "template": {
                    "type": "BodyTemplate7",
                    "token": "SampleTemplate_3476",
                    "backButton": "VISIBLE",
                    "title": "本日の活動時間：8時間21分",
                    "backgroundImage": {
                        "contentDescription": "家",
                        "sources": [
                            {
                                "url": "https://mam3104.com/static/image/qol/VerL/2-B.jpg"
                            }
                        ]
                    },
                    "image": {
                        "contentDescription": "園児",
                        "sources": [
                            {
                                "url": URL
                            }
                        ]
                    }
                }
            }
        ],
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_image3(title, output, reprompt_text, should_end_session):
    rand = random.randrange(1, 3)
    if rand == 1:
        URL = "https://mam3104.com/static/image/qol/VerL/5.png"
    elif rand == 2:
        URL = "https://mam3104.com/static/image/qol/VerL/6-EX.png"
    elif rand == 3:
        URL = "https://mam3104.com/static/image/qol/VerL/6.png"
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Standard',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
         "directives": [
            {
                "type": "Display.RenderTemplate",
                "template": {
                    "type": "BodyTemplate7",
                    "token": "SampleTemplate_3476",
                    "backButton": "VISIBLE",
                    #"title": "ふつう",
                    "backgroundImage": {
                        "contentDescription": "教室",
                        "sources": [
                            {
                                "url": "https://mam3104.com/static/image/qol/VerL/5-B.jpg"
                            }
                        ]
                    },
                    "image": {
                        "contentDescription": "学生",
                        "sources": [
                            {
                                "url": URL
                            }
                        ]
                    }
                }
            }
        ],
        'shouldEndSession': should_end_session
    }

def build_speechlet_response_image4(title, output, reprompt_text, should_end_session):
    rand = random.randrange(1, 3)
    if rand == 1:
        URLB = "https://mam3104.com/static/image/qol/VerL/7-B.jpg"
        URL = "https://mam3104.com/static/image/qol/VerL/7.png"
    elif rand == 2:
        URLB = "https://mam3104.com/static/image/qol/VerL/8-B.jpg"
        URL = "https://mam3104.com/static/image/qol/VerL/8.png"
    elif rand == 3:
        URLB = "https://mam3104.com/static/image/qol/VerL/8-EX-B.jpg"
        URL = "https://mam3104.com/static/image/qol/VerL/8-EX.png"
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Standard',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
         "directives": [
            {
                "type": "Display.RenderTemplate",
                "template": {
                    "type": "BodyTemplate7",
                    "token": "SampleTemplate_3476",
                    "backButton": "VISIBLE",
                    #"title": "かぁす",
                    "backgroundImage": {
                        "contentDescription": "大学生-社会人",
                        "sources": [
                            {
                                "url": URLB
                            }
                        ]
                    },
                    "image": {
                        "contentDescription": "大学生-社会人",
                        "sources": [
                            {
                                "url": URL
                            }
                        ]
                    }
                }
            }
        ],
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_sorry(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Standard',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
         "directives": [
            {
                "type": "Display.RenderTemplate",
                "template": {
                    "type": "BodyTemplate7",
                    "token": "SampleTemplate_3476",
                    "backButton": "VISIBLE",
                    "title": "ごめんなさい",
                    "backgroundImage": {
                        "contentDescription": "背景",
                        "sources": [
                            {
                                "url": "https://mam3104.com/static/image/qol/bg3.png"
                            }
                        ]
                    },
                    "image": {
                        "contentDescription": "マンドラゴラ",
                        "sources": [
                            {
                                "url": "https://mam3104.com/static/image/qol/sorry.png"
                            }
                        ]
                    }
                }
            }
        ],
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "こんにちは！" \
                    "こちらは外出支援システムです。" \
                    "起動するスキルを教えてください。"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_launch(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "さようなら！"
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def score_intent(intent, session):

    card_title = "ScoreIntent"
    session_attributes = {}
    
    #score = random.randrange(1, 4)
    score = 2
    
    if score == 1:
        speech_output = "すごい" \
                        "今日はちゃんと運動できたね！" 
        reprompt_text = speech_output
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response_image1(card_title, speech_output, reprompt_text, should_end_session))
    elif score == 2:
        speech_output = "今日の活動時間は8時間21分。" \
                        "現在13532歩、歩いています。その調子で頑張りましょう！" 
        reprompt_text = speech_output
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response_image2(card_title, speech_output, reprompt_text, should_end_session))
    elif score == 3:
        speech_output = "うーん。" \
                        "今日はあまり運動できなかったね。" 
        reprompt_text = speech_output
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response_image3(card_title, speech_output, reprompt_text, should_end_session))
    elif score == 4:
        speech_output = "今日は忙しかったのかな？" \
                        "全く運動できなかったね。" 
        reprompt_text = speech_output
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response_image4(card_title, speech_output, reprompt_text, should_end_session))

def rank_intent(intent, session):

    card_title = "RankIntent"
    session_attributes = {}

    speech_output = "ごめんなさい。" \
                    "このスキルはまだ実装されていません" 
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_sorry(
        card_title, speech_output, reprompt_text, should_end_session))
        
def game_intent(intent, session):

    card_title = "GameIntent"
    session_attributes = {}

    speech_output = "ごめんなさい。" \
                    "このスキルはまだ実装されていません" 
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_sorry(
        card_title, speech_output, reprompt_text, should_end_session))

def return_intent(intent, session):

    card_title = "ReturnIntent"
    session_attributes = {}

    speech_output = "操作を選択してください"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_launch(
        card_title, speech_output, reprompt_text, should_end_session))

def finish_intent(intent, session):

    card_title = "FinishIntent"
    speech_output = "さようなら"
    should_end_session = True
    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "ScoreIntent":
        return score_intent(intent, session)
    elif intent_name == "RankIntent":
        return rank_intent(intent, session)
    elif intent_name == "GameIntent":
        return game_intent(intent, session)
    elif intent_name == "ReturnIntent":
        return return_intent(intent, session)
    elif intent_name == "FinishIntent":
        return finish_intent(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        #return handle_session_end_request()
        return finish_intent(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
    elif event['request']['type'] == "Display.ElementSelected":
        return element_selected_handler(event['request'], event['session'])
        
# --------------- 自作 handler ------------------

def element_selected_handler(handler_input,session):
    
    token = handler_input['token']
    intent = {}
    if token == "list1":
        return score_intent(intent, session)
    elif token == "list2":
        return rank_intent(intent, session)
    elif token == "list3":
        return game_intent(intent, session)
    elif token == "list4":
        return finish_intent(intent, session)
    