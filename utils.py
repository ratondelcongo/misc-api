import requests
from bs4 import BeautifulSoup

ZODIAC_NAMES = {
    "aries": 1,
    "tauro": 2,
    "geminis": 3,
    "cancer": 4,
    "leo": 5,
    "virgo": 6,
    "libra": 7,
    "escorpio": 8,
    "sagitario": 9,
    "capricornio": 10,
    "acuario": 11,
    "piscis": 12
}

ZODIAC_NUMBERS = {
    "1": "aries",
    "2": "tauro",
    "3": "geminis",
    "4": "cancer",
    "5": "leo",
    "6": "virgo",
    "7": "libra",
    "8": "escorpio",
    "9": "sagitario",
    "10": "capricornio",
    "11": "acuario",
    "12": "piscis"
}


def getHoroscopeBySign(zodiac_sign: str):
    try:
        res = requests.get(
            f'https://www.lavanguardia.com/horoscopo/signos-zodiaco-{zodiac_sign}/horoscopo-diario')
        soup = BeautifulSoup(res.text, 'html.parser')
        data = soup.select(
            '#main > div > section.section-holder.sign-detail-section > div > div > div > p')
        return data[0].text.strip()
    except:
        return 'No registrado'


def getHoroscopeAll():
    result = []
    try:
        for e in ZODIAC_NUMBERS:
            object = {}
            res = requests.get(
                f'https://www.lavanguardia.com/horoscopo/signos-zodiaco-{ZODIAC_NUMBERS[e]}/horoscopo-diario')
            soup = BeautifulSoup(res.text, 'html.parser')
            horoscope = soup.select(
                '#main > div > section.section-holder.sign-detail-section > div > div > div > p')[0].text.strip()
            dates = soup.select(
                '#main > div > section.section-holder.sign-detail-section > header > div.title-group > div > p')[0].text.strip()
            object['sign'] = ZODIAC_NUMBERS[e]
            object['horoscope'] = horoscope
            object['dates'] = dates
            result.append(object)
    except:
        None
    return result


def getTablaClasificatoriasQatar():
    result = []

    res = requests.get(
        f'https://www.futbolperuano.com/eliminatorias/tabla-de-posiciones')
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        for i in range(4):
            selector = f'#p_score_contenido_TorneoTabs_collapse1 > div > table > tbody > tr:nth-child({i + 1}) > td.equipo.text-left > span.d-md-none'
            data = soup.select(selector)
            pais = data[0].text.strip()
            selector = f'#p_score_contenido_TorneoTabs_collapse1 > div > table > tbody > tr:nth-child({i + 1}) > td:nth-child(9)'
            data = soup.select(selector)
            dg = data[0].text.strip()
            selector = f'#p_score_contenido_TorneoTabs_collapse1 > div > table > tbody > tr:nth-child({i + 1}) > td:nth-child(10)'
            data = soup.select(selector)
            puntos = data[0].text.strip()

            object = {}
            object['pais'] = pais
            object['dg'] = dg
            object['puntos'] = puntos

            result.append(object)

        selector = f'#p_score_contenido_TorneoTabs_collapse1 > div > table > tbody > tr:nth-child(5) > td.equipo.text-left > a > span.d-md-none'
        data = soup.select(selector)
        pais = data[0].text.strip()
        selector = f'#p_score_contenido_TorneoTabs_collapse1 > div > table > tbody > tr:nth-child(5) > td:nth-child(9)'
        data = soup.select(selector)
        dg = data[0].text.strip()
        selector = f'#p_score_contenido_TorneoTabs_collapse1 > div > table > tbody > tr:nth-child(5) > td:nth-child(10)'
        data = soup.select(selector)
        puntos = data[0].text.strip()

        object = {}
        object['pais'] = pais
        object['dg'] = dg
        object['puntos'] = puntos

        result.append(object)

        for i in range(5):
            selector = f'#p_score_contenido_TorneoTabs_collapse1 > div > table > tbody > tr:nth-child({i + 6}) > td.equipo.text-left > span.d-md-none'
            data = soup.select(selector)
            pais = data[0].text.strip()
            selector = f'#p_score_contenido_TorneoTabs_collapse1 > div > table > tbody > tr:nth-child({i + 6}) > td:nth-child(9)'
            data = soup.select(selector)
            dg = data[0].text.strip()
            selector = f'#p_score_contenido_TorneoTabs_collapse1 > div > table > tbody > tr:nth-child({i + 6}) > td:nth-child(10)'
            data = soup.select(selector)
            puntos = data[0].text.strip()

            object = {}
            object['pais'] = pais
            object['dg'] = dg
            object['puntos'] = puntos

            result.append(object)
    except:
        None
    return result
