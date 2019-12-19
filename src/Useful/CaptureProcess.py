import requests
from lxml import etree, html

from .CaptchaSolver import getCaptchaResponse, clickAction
from .Tools import getCaptchaId

def capture(firstResponse, url, pnParts):

    numberDigitYear = "{}-{}.{}".format(pnParts['number'], pnParts['verification'], pnParts['year'])
    forum = pnParts['forum']
    cnj = "{}.{}.{}.{}".format(numberDigitYear, pnParts['area'], pnParts['court'], forum)

    hashResult = getCaptchaResponse(firstResponse, url)

    querystring = {
        'conversationId':'',
        'dadosConsulta.localPesquisa.cdLocal':'-1',
        'cbPesquisa':'NUMPROC',
        'dadosConsulta.tipoNuProcesso':'UNIFICADO',
        'numeroDigitoAnoUnificado':numberDigitYear,
        'foroNumeroUnificado':pnParts['forum'],
        'dadosConsulta.valorConsultaNuUnificado':cnj,
        'dadosConsulta.valorConsulta':'',
        'uuidCaptcha':getCaptchaId(firstResponse),
         'g-recaptcha-response':hashResult
        }

    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "esaj.tjsp.jus.br",
        'Referer': "https://esaj.tjsp.jus.br/cpopg/open.do",
        'Upgrade-Insecure-Requests': "1",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    return clickAction(url, headers, querystring, hashResult)