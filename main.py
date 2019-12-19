from src.Useful.Parser import getMovements, getParts, getValues
from src.Useful.Tools import getProcessNumber, getFirstResponse, splitProcess
from src.Useful.CaptureProcess import capture

url = "https://esaj.tjsp.jus.br/cpopg/open.do"

# processNumber = '0011173-68.2018.8.26.0041'
processNumber = getProcessNumber('Insert the process\'s number: ')

processNumberParts = splitProcess(processNumber)

firstResponse = getFirstResponse(url)

html = capture(firstResponse.text, url, processNumberParts)

# html = getFirstResponse('http://localhost:8000/tjsp.html').text # for parser

print(getMovements(html))

print(getParts(html))

print(getValues(html))