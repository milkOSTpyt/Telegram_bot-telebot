from requests_html import HTMLSession


def forecast(data):
    """ Функция парсит погоду и отдает ее вместе со смайликами """

    #Смайлы
    rain = u'\U00002614'
    snowflake = u'\U00002744'
    clearSky = u'\U00002600'
    clouds = u'\U00002601'
    fewClouds = u'\U000026C5'

    #xpath 
    time_xpath ='/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/\
    div/div[1]/div/div[1]//span//text()'
    weather_xpath ='/html/body/section/div[2]//div[1]/div[2]/div[1]/div[2]/div/\
    div[1]/div/div[3]//span[1]//text()'

    url = f'https://www.gismeteo.by/weather-{data}/'
    session = HTMLSession()
    response = session.get(url)
    time = response.html.xpath(time_xpath)
    weather = response.html.xpath(weather_xpath)
    data_text = response.html.find('.tooltip')[3:11]
    my_str = 'Погода на сегодня:\n'
    for t, w, d in zip(time, weather, data_text):
        if 'дождь' in d.attrs['data-text'].lower():
            my_str += f'{t}.00 : {w} {rain}\n'
        elif 'ясно' in d.attrs['data-text'].lower():
            my_str += f'{t}.00 : {w} {clearSky}\n'
        elif 'малооблачно' in d.attrs['data-text'].lower():
            my_str += f'{t}.00 : {w} {fewClouds}\n'
        elif 'пасмурно' or 'облачно' in d.attrs['data-text'].lower():
            my_str+=f'{t}.00 : {w} {clouds}\n'
    return my_str


def openssource():
    """ Функция парсит первую страницу сайта https://openssource.biz/ """
    title_text = '✏️OPENSSOURCE:\n\n'
    url = 'https://openssource.biz/'
    with HTMLSession() as session:
        response = session.get(url)
    title = response.html.xpath('//h2/a//text()')
    links = response.html.xpath('//div/h2/a/@href')
    for t, l in zip(title, links):
        title_text+=f'▪️{t}\n{l}\n\n'
    return title_text


def belmeta(lang):
    """ Функция парсит вакансии за последние 3 дня """
    url = f'https://belmeta.com/vacansii?q={lang}&df=3&sort=date'
    with HTMLSession() as session:
        response = session.get(url)
    q=int(response.html.xpath('//section//div[6]/div[1]//text()')[0].split()[2])
    text = response.html.xpath('//div[1]/div[2]/h2/a')[:q]
    links = response.html.xpath('//div[1]/div[2]/h2/a/@href')[:q]
    titles = f'🔍Вакансии({q}):\n\n'
    for t, l in zip(text, links):
        titles+=f'▪️{t.text}\n https://belmeta.com/{l}\n'
    return titles