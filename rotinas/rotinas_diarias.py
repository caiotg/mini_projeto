from dados_yf import puxando_cotacoes
from scraping_braziljournal import scraping_brazil_journal


def atualizar_rotinas():

    puxando_cotacoes()
    scraping_brazil_journal()


atualizar_rotinas()
