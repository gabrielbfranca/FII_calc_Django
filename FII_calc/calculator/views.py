from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_html_content(tag):
    import requests
    html_content = requests.get("https://www.fundsexplorer.com.br/funds/" + str(tag))
    return html_content

def calculator( ticker, renda=None, t=None, C=None):
    from bs4 import BeautifulSoup
    html_content = get_html_content(ticker)
    soup = BeautifulSoup(html_content.text, "html.parser")

    result = dict()
    result["preco"] = float(soup.find("span", attrs={"class":"price"}).text.replace('\n', '').replace("R$","").replace(" ", "").replace(",", "."))
    result["dividends"] = float(soup.find_all("span", attrs={"class":"indicator-value"})[1].text.replace("R$", "").replace(" ", "").replace(",", "."))
    if renda == '':
        result["renda"] = 12 * float(t) * (result["dividends"]/result["preco"]) * float(C)

    elif t == '':

        result["t"] = (float(renda)/((result["dividends"]/result["preco"]) * float(C)))/12

    elif C == '':

        result["C"] = (float(renda) * result["preco"]) / (12 * float(t) * (result["dividends"]))

    return result

def detect_and_validate_empty_value(renda, t, C):
    dado = 0
    value = False
    if (C =='' and t == '') or (C == '' and renda == '') or (renda =='' and t == ''):
        value = True
    elif renda == '':
        dado = 1
        value = False
    elif t == '':
        dado = 2
        value = False
    elif C == '':
        dado = 3
        value = False
    gay = {'dado':dado, 'value':value, 'renda':renda, 't':t, 'C':C }         
    return gay
    

    

def validar_tag(tag):
    from bs4 import BeautifulSoup
    siglas = []
    validate = True
    html_content = get_html_content('')
    soup = BeautifulSoup(html_content.text, "html.parser")
    FIIs = soup.find_all("div", attrs={"class":"col-md-3 col-xs-12"})
    for FII in FIIs:
        name = FII.div["id"][5:-1] + "1"
        siglas.append(name) 
    if tag in siglas:
        validate = True
    else:
        validate = False
    return validate

def home(request):
    calculado = {}
    if "ticker" in request.GET:
        # fetch weather data
        tag = request.GET.get("ticker")
        renda = request.GET.get("renda")
        t = request.GET.get("tempo")
        C = request.GET.get("Capital")
        detector = detect_and_validate_empty_value(renda=renda, t=t, C=C)
        validate = validar_tag(tag)
        if not validate or detector['value']:
            calculado = False
        else:
            calculado = calculator(tag, detector['renda'], detector['t'], detector['C'])
            calculado['dado'] = detector['dado']
            print(detector)
            print(calculado)
        
    return render(request, "core/home.html", {'calculado': calculado})
