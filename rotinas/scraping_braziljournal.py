from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def scraping_brazil_journal():

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    lista_dfs = []

    urls_bj = {
        'WEGE3': 'https://braziljournal.com/?s=weg',
        'PETR4': 'https://braziljournal.com/?s=petrobras',
        'CEAB3': 'https://braziljournal.com/?s=c%26a'
    }

    for ticker, url in urls_bj.items():

        driver.get(url)

        todas_noticias = driver.find_element('xpath', '/html')

        html_noticias = todas_noticias.get_attribute('outerHTML')

        soup = BeautifulSoup(html_noticias, 'html.parser')

        caixa_noticias = soup.find_all('figcaption', class_='boxarticle-infos')

        df_noticias = pd.DataFrame(
            columns=['manchete', 'subtopico', 'link', 'empresa'], index=[0, 1, 2])

        for i, noticia in enumerate(caixa_noticias):

            manchete = noticia.find('h2', class_='boxarticle-infos-title').text
            subtopico = noticia.find('p', class_='boxarticle-infos-tag').text
            link = noticia.find(
                'h2', class_='boxarticle-infos-title').a['href']

            df_noticias.loc[i, 'manchete'] = manchete
            df_noticias.loc[i, 'subtopico'] = subtopico
            df_noticias.loc[i, 'link'] = link
            df_noticias.loc[i, 'ticker'] = ticker

            if i == 2:

                break

        lista_dfs.append(df_noticias)

    driver.quit()

    noticias = pd.concat(lista_dfs, ignore_index=True)

    noticias.to_csv(fr'dados\noticias.csv', index=False)
