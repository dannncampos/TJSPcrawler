import re
import string
import json

from lxml import etree, html
from .Tools import clearContent

def getMovements(htmlContent):
    movs = []
    movements = html.fromstring(htmlContent).xpath('//*[@id="tabelaUltimasMovimentacoes"]/tr')
    for row in movements:
        data = clearContent(row.xpath('./td[1]/text()'))
        movimentacao = clearContent(row.xpath('string(./td[3])'))
        movs.append({'data':data, 'movimentacao':movimentacao})
    return movs

def getParts(htmlContent):
    parts = []
    trParts = html.fromstring(htmlContent).xpath('//*[@id="tablePartesPrincipais"]//tr')
    for row in trParts:
        typePart = clearContent(row.xpath('./td[1]/span/text()'))
        name = clearContent(row.xpath('string(./td[2])'))
        parts.append({'tipo':typePart, 'nome':name})
    return parts

def getValues(htmlContent):
    values = []
    trValues = html.fromstring(htmlContent).xpath('//*[@class="secaoFormBody" and @id!="secaoFormConsulta"]/tbody/tr')
    for row in trValues:
        label = clearContent(row.xpath('./td[1]/label/text()'))
        value = clearContent(row.xpath('string(./td[2])'))
        values.append({'chave':label, 'valor':value})
    return values