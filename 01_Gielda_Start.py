from stockmarkettools import *
from selenium import webdriver


if __name__ == '__main__':
    # get_stock_all('infosys',time='1y',sure='True').make_graph()

    # micr=get_stock_all('infosys',time='1d').info
    # print(micr)

    # get_stock_all.make_graph_two('infosys','wipro','1y')

    # https://stooq.pl/q/l/?s=_stat_plws_up_+_stat_plws_dw_&f=sd2t2ohlcm2vr&h&e=csv

    browser = webdriver.Firefox()
    browser.get('https://google.com')
    