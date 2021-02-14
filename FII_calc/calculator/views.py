from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
# Create your views here.
siglas = ['ABCP11', 'AFCR11', 'AFHI11', 'AFOF11', 'AIEC11', 'ALMI11', 'ALZR11', 'ANCR111', 'AQLL11', 'ARCT11', 'ARFI111', 'ARRI11',
 'ATCR11', 'ATSA11',
 'ATWN11',
 'BARI11',
 'BBFI111',
 'BBFO11',
 'BBPO11',
 'BBRC11',
 'BBVJ11',
 'BCFF11',
 'BCIA11',
 'BCRI11',
 'BICR11',
 'BLCP11',
 'BLMG11',
 'BLMO11',
 'BLMR11',
 'BMII11',
 'BMLC11',
 'BMLC111',
 'BNFS11',
 'BPFF11',
 'BPML11',
 'BRCO11',
 'BRCR11',
 'BREV11',
 'BRHT111',
 'BRIP11',
 'BRLA11',
 'BTAL11',
 'BTCR11',
 'BTGM11',
 'BTLG11',
 'BVAR11',
 'BZLI11',
 'CARE11',
 'CBOP11',
 'CEOC11',
 'CJCT11',
 'CNES11',
 'CPFF11',
 'CPTS11',
 'CRFF11',
 'CTXT11',
 'CVBI11',
 'CXCE111',
 'CXRI11',
 'CXTL11',
 'DEVA11',
 'DMAC11',
 'DOMC11',
 'DOVL111',
 'DRIT111',
 'EDFO111',
 'EDGA11',
 'EGYR11',
 'ELDO111',
 'ERCR11',
 'EURO11',
 'FAED11',
 'FAMB111',
 'FATN11',
 'FCAS11',
 'FCFL11',
 'FEXC11',
 'FFCI11',
 'FIGS11',
 'FIIB11',
 'FIIP111',
 'FINF11',
 'FIVN11',
 'FLMA11',
 'FLRP11',
 'FMOF11',
 'FOFT11',
 'FPAB11',
 'FPNG11',
 'FVBI11',
 'FVPQ11',
 'GALG11',
 'GCFF11',
 'GGRC11',
 'GRLV11',
 'GSFI11',
 'GTWR11',
 'HABT11',
 'HBRH11',
 'HBTT11',
 'HCRI11',
 'HCST11',
 'HCTR11',
 'HFOF11',
 'HGBS11',
 'HGCR11',
 'HGFF11',
 'HGLG11',
 'HGPO11',
 'HGRE11',
 'HGRU11',
 'HLOG11',
 'HMOC11',
 'HOSI11',
 'HPDP11',
 'HRDF11',
 'HREC11',
 'HSAF11',
 'HSLG11',
 'HSML11',
 'HSRE11',
 'HTMX11',
 'HUSC11',
 'IBFF11',
 'IFID11',
 'IFIE11',
 'IRDM11',
 'JFLL11',
 'JPPA11',
 'JRDM11',
 'JSRE11',
 'KEVE11',
 'KFOF11',
 'KINP11',
 'KISU11',
 'KNCR11',
 'KNHY11',
 'KNIP11',
 'KNRE11',
 'KNRI11',
 'KNSC11',
 'LASC11',
 'LGCP11',
 'LUGG11',
 'LVBI11',
 'MALL11',
 'MAXR11',
 'MBRF11',
 'MCCI11',
 'MFAI11',
 'MFII11',
 'MGCR11',
 'MGFF11',
 'MGHT11',
 'MORE11',
 'MXRF11',
 'NCHB11',
 'NEWL11',
 'NEWU11',
 'NSLU11',
 'NVHO11',
 'NVIF111',
 'ONEF11',
 'ORPD11',
 'OUCY11',
 'OUFF11',
 'OUJP11',
 'OULG11',
 'OURE11',
 'PABY11',
 'PATC11',
 'PATL11',
 'PLCR11',
 'PLRI11',
 'PORD11',
 'PQAG11',
 'PQDP11',
 'PRSV11',
 'PRTS11',
 'PVBI11',
 'QAGR11',
 'QAMI11',
 'QIFF11',
 'QMFF11',
 'RBBV11',
 'RBCB11',
 'RBCO11',
 'RBDS11',
 'RBED11',
 'RBFF11',
 'RBGS11',
 'RBIR11',
 'RBIV11',
 'RBRD11',
 'RBRF11',
 'RBRL11',
 'RBRP11',
 'RBRR11',
 'RBRS11',
 'RBRY11',
 'RBTS11',
 'RBVA11',
 'RBVO11',
 'RCFA11',
 'RCRB11',
 'RDES11',
 'RDPD11',
 'RECH11',
 'RECR11',
 'RECT11',
 'RECX11',
 'RELG11',
 'RFOF11',
 'RNDP11',
 'RNGO11',
 'RSPD11',
 'RVBI11',
 'RZAK11',
 'RZTR11',
 'SAAG11',
 'SADI11',
 'SAIC111',
 'SARE11',
 'SCPF11',
 'SDIL11',
 'SDIP11',
 'SEQR11',
 'SFND11',
 'SHDP111',
 'SHOP11',
 'SHPH11',
 'SPTW11',
 'SPVJ11',
 'STRX11',
 'TBOF11',
 'TEPP11',
 'TGAR11',
 'THRA11',
 'TORD11',
 'TRNT11',
 'TRXF11',
 'TRXL11',
 'UBSR11',
 'URPR11',
 'VCJR11',
 'VERE11',
 'VGHF11',
 'VGIP11',
 'VGIR11',
 'VIFI11',
 'VILG11',
 'VINO11',
 'VISC11',
 'VLOL11',
 'VOTS11',
 'VPSI11',
 'VRTA11',
 'VSHO11',
 'VTLT11',
 'VVPR11',
 'WPLZ11',
 'WTSP111',
 'XPCI11',
 'XPCM11',
 'XPHT11',
 'XPIN11',
 'XPLG11',
 'XPML11',
 'XPPR11',
 'XPSF11',
 'XTED11',
 'YCHY11']

def get_html_content(tag):
    html_content = requests.get("https://www.fundsexplorer.com.br/funds/" + str(tag))
    return html_content

def calculator( ticker, renda=None, t=None, C=None):
    html_content = get_html_content(ticker)
    soup = BeautifulSoup(html_content.text, "html.parser")

    result = dict()
    result["preco"] = float(new_soup.find("span", attrs={"class":"price"}).text.replace('\n', '').replace("R$","").replace(" ", "").replace(",", "."))
    result["dividendos"] = float(new_soup.find_all("span", attrs={"class":"indicator-value"})[1].text.replace("R$", "").replace(" ", "").replace(",", "."))
    if renda == None:
        result["renda"] = 12 * t * (result["dividends"]/result["preco"]) * C

    elif t == None:

        result["t"] = (renda/((result["dividends"]/result["preco"]) * C))/12

    elif C == None:

        result["C"] = renda / (12 * t * (result["dividends"]/result["preco"]))

    return result

def detect_and_validate_empty_value(renda=0, t=0, C=0):
    dado = 0
    if C + t + renda == 0:
        return True
    elif C + t ==0 or C + renda == 0 or renda + t == 0:
        return True

    if renda == 0:
        dado = 1
    elif t == 0:
        dado = 2
    elif C == 0:
        dado = 3
    return dado, False
    

    

def validar_tag(tag):
    if tag in siglas:
        return True
    else:
        return False



def home(request):
    calculado = None
    dado = None
    
    if "ticker" in request.GET:
        # fetch weather data
        tag = request.GET.get("ticker")
        renda = request.GET.get("renda")
        t = request.GET.get("tempo")
        C = request.GET.get("Capital")
        if detect_empty_value(preco, t, C):
            pass # send message error


        if validar_tag(tag) == False:
            pass # send message error to html 
        else:
            calculado = calculator(tag, preco, t, C)
    return render(request, "core/home.html", {'calculado': calculado}, {'dado': dado})
    