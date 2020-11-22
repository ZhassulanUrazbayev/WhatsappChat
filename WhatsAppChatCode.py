# !/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import datetime
import schedule
import time
import json

waInstance = "waInstance9696"

apiToken = "7d12628382146e6cb91325fa7eadc21b72aa5adfc56659cc54"

creatGroupUrl = "https://api.green-api.com/" + waInstance + "/createGroup/" + apiToken

sendMessageUrl = "https://api.green-api.com/" + waInstance + "/sendMessage/" + apiToken

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().strftime("%m")
year = datetime.datetime.now().strftime("%Y")

countCharNumber = 1

chatId = "77474563370-1605778950@g.us"

# creatGroup = "{\r\n\t\"groupName\": \"%s.%s.%s cағ: 19-00 тегін мастер класс %d\",\r\n    \"chatIds\": [\r\n        \"77474563370@c.us\"\r\n\t]\r\n}\r\n" % (day, month, year, countCharNumber)
#
# sendMessage = "{\r\n\t\"chatId\": \"77474563370-1605778950@g.us\",\r\n\t\"message\": \"I use Green-API to send this message to you!\"\r\n}"
#
# sendMessageAt1850 = "{\r\n\t\"chatId\": \"77474563370-1605778950@g.us\",\r\n\t\"message\": \"I use Green-API to send this message to you 18-50 !\"\r\n}"
#
# sendMessageAt1900 = "{\r\n\t\"chatId\": \"77474563370-1605778950@g.us\",\r\n\t\"message\": \"I use Green-API to send this message to you 19-00 !\"\r\n}"

headers = {
    'Content-Type': 'application/json'
}

# print(datetime.datetime.now())
print(chatId)
print(countCharNumber)


def createGruop1(chatNumber):
    creatGroup = "{\r\n\t\"groupName\": \"Қуаныш Шонбайдың тегін мастер классы %d\",\r\n    \"chatIds\": [\r\n        \"77474563370@c.us\"\r\n\t]\r\n}\r\n" % (
        chatNumber)

    creatGroupResponse = requests.request("POST", creatGroupUrl, headers=headers, data=creatGroup.encode('utf8'))

    y = json.loads(creatGroupResponse.text.encode('utf8'))

    # print(y['chatId'])
    # print(y['groupInviteLink'])

    print(creatGroupResponse.text.encode('utf8'))

    global chatId
    global countCharNumber
    chatId = y['chatId']
    countCharNumber = chatNumber + 1


def sendMessageAt1850(chatId):
    sendMessageAt1850 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use Green-API to send this http://stackoverflow.com to you 18-50 !\"\r\n}" % (
        chatId)

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1850.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print(chatId)

    print(sendMessageAt1850)

    print("I'm working at 18-50")


def sendMessageAt1900(chatId):
    sendMessageAt1900 = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"I use Green-API to send this http://stackoverflow.com to you 19-00 !\"\r\n}" % (
        chatId)

    sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers,
                                           data=sendMessageAt1900.encode('utf8'))

    y = json.loads(sendMessageResponse.text.encode('utf8'))

    print(y["idMessage"])

    print(sendMessageResponse.text.encode('utf8'))

    print("I'm working at 19-00")


# def createGroup():
#     global countCharNumber
#     createGruop1(countCharNumber)

def jobsendMessageAt1850():
    global chatId
    sendMessageAt1850(chatId)


def jobsendMessageAt1900():
    global chatId
    sendMessageAt1900(chatId)


# schedule.every().day.at("16:37").do(createGroup)
schedule.every().day.at("21:00").do(jobsendMessageAt1850)
schedule.every().day.at("21:01").do(jobsendMessageAt1900)

while True:
    schedule.run_pending()
    time.sleep(1)

# sendMessageResponse = requests.request("POST", sendMessageUrl, headers=headers, data = sendMessage)

# creatGroupResponse = requests.request("POST", creatGroupUrl, headers=headers, data = creatGroup)
# y = json.loads(sendMessageResponse.text.encode('utf8'))
#
# print(y["idMessage"])
#
# print(sendMessageResponse.text.encode('utf8'))
