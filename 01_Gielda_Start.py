from selenium import webdriver
import os
import time

# function to string into list with space as separator
def String_to_list(string):
    li = list(string.split(" "))
    return li

# function to return key for any value
def get_dic_key(val, my_dic):
    for key, value in my_dic.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def zaladuj_tabele_trendy_naj(trend, okres, rozmiar):
    """
    Procedura do ladowania trendow ze strony biznesradar.pl. Jako wynik zwraca tabele z trendami w zadanym okresie i trendem (spadki, wzrosty).
    trend (boolean):
        False - wzrosty
        True - spadki

    okres (integer): tydzien, miesiac, 6 miesiacy, itd
    rozmiar (integer): ilosc rekordow do popbrania (jak na razie max na stronie to 30 wierszy w sekcji tabeli)
    """
    # Selection of web browser
    driver = webdriver.Firefox()
    driver.get('https://www.biznesradar.pl/stopy-zwrotu/akcje_gpw')
    
    sortOrder = driver.find_element_by_xpath('//*[@id="right-content"]/div/table/tbody/tr[1]/th[{}]/a'.format(okres))
    webdriver.ActionChains(driver).click(sortOrder).perform()
    time.sleep(3)
    
    if trend:
        sortOrder = driver.find_element_by_xpath('//*[@id="right-content"]/div/table/tbody/tr[1]/th[{}]/a'.format(okres))
        webdriver.ActionChains(driver).click(sortOrder).perform()
        time.sleep(3)

    tabela = []
    for wiersz in range(1,rozmiar):
        tabela.append(String_to_list(driver.find_element_by_xpath('//*[@id="right-content"]/div/table/tbody/tr[{}]'.format(wiersz)).text))

    for wiersz in tabela:
        if "%" in wiersz[1]:
            wiersz.insert(1,"")

    driver.close()

    return tabela

def drukuj_tabele_trendy_naj(tabela, trend, okres, rozmiar):
    """
    Procedura do drukowania trendow podanych w zmiennej tabela.
    trend (boolean):
        False - wzrosty
        True - spadki

    okres (integer): tydzien, miesiac, 6 miesiacy, itd
    rozmiar (integer): ilosc rekordow do popbrania (jak na razie max na stronie to 30 wierszy w sekcji tabeli)
    """
    print("Lista {} spolek. Trend: {}. Okres: {}".format(rozmiar, get_dic_key(trend,trendy_trend), get_dic_key(okres, trendy_okres)))
    for wiersz in tabela:
        if tabela.index(wiersz) == 0:
            print((25+10*10) * "-")
            print(" {:>3} ".format("Poz") + "{0:^20} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9} {6:^9} {7:^9} {8:^9} {9:^9} {10:^9}".format(wiersz[0], wiersz[1], wiersz[2], wiersz[3], wiersz[4], wiersz[5], wiersz[6], wiersz[7], wiersz[8], wiersz[9], wiersz[10]))
            print((25+10*10) * "-")
        else:
            print("{:>3}. ".format(tabela.index(wiersz)) + "{0:<4} {1:<15} {2:>9} {3:>9} {4:>9} {5:>9} {6:>9} {7:>9} {8:>9} {9:>9} {10:>9} {11:>9}".format(wiersz[0], wiersz[1], wiersz[2], wiersz[3], wiersz[4], wiersz[5], wiersz[6], wiersz[7], wiersz[8], wiersz[9], wiersz[10] , wiersz[11]))
        
    print()

def moje_glowne_menu():
    
    selection = 12 
    while selection not in range(0, 11):
        os.system('clear')
        print('+' + 102*'-' + '+')
        print("| {:^100} |".format('Main Menu'))
        print('+' + 102*'-' + '+')
        print("| {:^100} |".format(''))
        print("| {:10}{:<90} |".format('','1: Tabela tredow wzrosty za tydzinen'))
        print("| {:10}{:<90} |".format('','2: Tabela tredow spadki za tydzinen'))
        print("| {:10}{:<90} |".format('','3: Tabela tredow wzrosty za miesiac'))
        print("| {:10}{:<90} |".format('','4: Tabela tredow spadki za miesiac'))
        print("| {:10}{:<90} |".format('','5: Tabela tredow wzrosty za 3 miesiace'))
        print("| {:10}{:<90} |".format('','6: Tabela tredow spadki za 3 miesiace'))
        print("| {:10}{:<90} |".format('','7: Tabela tredow wzrosty za 6 miesiecy'))
        print("| {:10}{:<90} |".format('','8: Tabela tredow spadki za 6 miesiecy'))
        print("| {:10}{:<90} |".format('','9: Tabela tredow wzrosty za rok'))
        print("| {:9}{:<91} |".format('','10: Tabela tredow spadki za rok'))
        print("| {:^100} |".format(''))
        print('+' + 102*'-' + '+')
        
        input_value = input("Please select option (Select 0 to exit): ")
        if input_value == "":
            print('Wrong selection, please try again')
            input("Press [Enter] to continue")
            selection = 100
        else:
            selection = int(input_value)

    if selection == 1:
        os.system('clear')
        tabela = zaladuj_tabele_trendy_naj(trendy_trend['wzrosty'], trendy_okres['tydzien'], trendy_zakres)
        drukuj_tabele_trendy_naj(tabela, trendy_trend['wzrosty'], trendy_okres['tydzien'], trendy_zakres)
        input("Press [Enter] to continue")

    elif selection == 2:
        os.system('clear')
        tabela = zaladuj_tabele_trendy_naj(trendy_trend['spadki'], trendy_okres['tydzien'], trendy_zakres)
        drukuj_tabele_trendy_naj(tabela, trendy_trend['spadki'], trendy_okres['tydzien'], trendy_zakres)
        input("Press [Enter] to continue")
    
    elif selection == 3:
        os.system('clear')
        tabela = zaladuj_tabele_trendy_naj(trendy_trend['wzrosty'], trendy_okres['miesiac'], trendy_zakres)
        drukuj_tabele_trendy_naj(tabela, trendy_trend['wzrosty'], trendy_okres['miesiac'], trendy_zakres)
        input("Press [Enter] to continue")
    
    elif selection == 4:
        os.system('clear')
        tabela = zaladuj_tabele_trendy_naj(trendy_trend['spadki'], trendy_okres['miesiac'], trendy_zakres)
        drukuj_tabele_trendy_naj(tabela, trendy_trend['spadki'], trendy_okres['miesiac'], trendy_zakres)
        input("Press [Enter] to continue")

    elif selection == 5:
        os.system('clear')
        tabela = zaladuj_tabele_trendy_naj(trendy_trend['wzrosty'], trendy_okres['3 miesiace'], trendy_zakres)
        drukuj_tabele_trendy_naj(tabela, trendy_trend['wzrosty'], trendy_okres['3 miesiace'], trendy_zakres)
        input("Press [Enter] to continue")

    elif selection == 6:
        os.system('clear')
        tabela = zaladuj_tabele_trendy_naj(trendy_trend['spadki'], trendy_okres['3 miesiace'], trendy_zakres)
        drukuj_tabele_trendy_naj(tabela, trendy_trend['spadki'], trendy_okres['3 miesiace'], trendy_zakres)
        input("Press [Enter] to continue")

    elif selection == 7:
        os.system('clear')
        tabela = zaladuj_tabele_trendy_naj(trendy_trend['wzrosty'], trendy_okres['6 miesiecy'], trendy_zakres)
        drukuj_tabele_trendy_naj(tabela, trendy_trend['wzrosty'], trendy_okres['6 miesiecy'], trendy_zakres)
        input("Press [Enter] to continue")

    elif selection == 8:
        os.system('clear')
        tabela = zaladuj_tabele_trendy_naj(trendy_trend['spadki'], trendy_okres['6 miesiecy'], trendy_zakres)
        drukuj_tabele_trendy_naj(tabela, trendy_trend['spadki'], trendy_okres['6 miesiecy'], trendy_zakres)
        input("Press [Enter] to continue")
    
    elif selection == 9:
        os.system('clear')
        tabela = zaladuj_tabele_trendy_naj(trendy_trend['wzrosty'], trendy_okres['rok'], trendy_zakres)
        drukuj_tabele_trendy_naj(tabela, trendy_trend['wzrosty'], trendy_okres['rok'], trendy_zakres)
        input("Press [Enter] to continue")
    
    elif selection == 10:
        os.system('clear')
        tabela = zaladuj_tabele_trendy_naj(trendy_trend['spadki'], trendy_okres['rok'], trendy_zakres)
        drukuj_tabele_trendy_naj(tabela, trendy_trend['spadki'], trendy_okres['rok'], trendy_zakres)
        input("Press [Enter] to continue")

    return selection


if __name__ == '__main__':
    
    """
    Skryprt do prezentowania trendow notowan spolek z GWP na bazie danych prezentowanych na stronach biznesradar.pl.
    """
    # Parametry sotowania, prezentacji wynikow trendow.

    global trendy_zakres, trendy_okres, trendy_trend
    trendy_zakres = 27
    trendy_okres = {"tydzien": 2, "miesiac": 3, "3 miesiace": 4, "6 miesiecy": 5, "rok": 6}
    trendy_trend = {"spadki": True, "wzrosty": False}

    # Scrypt
    wybor = 1
    while wybor != 0:
        wybor = moje_glowne_menu()        

    print()
    print("Thank you for interaction :)")
    input("Press Any key and [Enter] or just [Enter] to Exit")    