import requests
import re
import json

def getProcessNumber(msg):
    while True:
        processNumber = str(input(msg))
        if len(processNumber) in (20, 25):
            break
        print('CNJ ({}) is not valid, please insert a valid process number with or without mask.'.format(processNumber))
    return processNumber

def getFirstResponse(url):
    querystring = {"":""}

    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "esaj.tjsp.jus.br",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    return requests.request("GET", url, headers=headers, params=querystring)

def getCaptchaId(htmlContent):
    return requests.get('https://esaj.tjsp.jus.br/cpopg/captchaControleAcesso.do').json()['uuidCaptcha']

def clearContent(content):
    return re.sub(r'[\t\r\n]', '', "".join(content)).strip()

def splitProcess(processNumber):
    pnParts = re.search('(?P<number>\d{7})[(\-)]?(?P<verification>\d{2})[(\.)]?(?P<year>\d{4})[(\.)]?(?P<area>\d)[(\.)]?(?P<court>\d{2})[(\.)]?(?P<forum>\d{4})$', processNumber)
    if pnParts is None:
        raise Exception('This CNJ ({}) is not valid.'.format(processNumber))
    return pnParts