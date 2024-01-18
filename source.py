import selenium
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def atstarpe(a):
    for i in range(0, a):
        print("")

def uzgaidiet(t, p):
    print("Uzgaidiet", end="")
    for i in range(0, p):
        print(".", end="", flush=True)
        time.sleep(t)

url = "https://www.1188.lv/varda-dienas"
saturs = requests.get(url)
if saturs.status_code == 200: # Vārda dienas paziņojums šodien
    lapa=bs4.BeautifulSoup(saturs.content, "html.parser")
    atrada=lapa.find_all(class_="names")
    svin = atrada[0].string
    atstarpe(20)
    print("Šodien vārda dienu svin:", svin)
    atstarpe(3)



 
service = Service()
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=option)

driver.get(url)
uzgaidiet(0.5, 5)
print("\r" + " " * 20, end="")

find = driver.find_element(By.CLASS_NAME, "css-47sehv") # Atbrīvojas no privātuma politikas loga
find.click()

find = driver.find_element(By.ID, "namedaysearch-nametext") #


atstarpe(1)
vards = input("Lūdzu ievadiet vārdu: ") # Izvēlētā vārda ievade
atstarpe(1)


while (vards.isalpha()) == False:
    vards = input("Lūdzu ievadiet vārdu: ") # Pārbauda vai vārds satur alfabēta burtus, kļūdas gadījumā atkārto vārda ievadi
find.send_keys(vards)

uzgaidiet(0.7, 6)
print("\r" + " " * 20, end="")
find.send_keys(Keys.ENTER)

url2 = driver.current_url # Jaunā url adrese


if url != url2: # Pārbauda vai vārds uzrakstīts pareizi, vai vispār eksistē caur url izmaiņām

    find = driver.find_element(By.CLASS_NAME, "selected-date")
    vardaDiena = find.text
    print("\r" + " " * 20, end="")

    saturs = requests.get(url2)

    if saturs.status_code == 200: # Izvada katra varda noziimes
        lapa=bs4.BeautifulSoup(saturs.content, "html.parser")
        nerakstitieVardirep = lapa.find_all("p" ,class_=["content", "name"]) # Nerakstitie vardi kalendara sakums
        varduNozimesVardi = lapa.find_all("h3", class_=["title", "content"])
        a = int(len(nerakstitieVardirep))
        nerakstitieVardi = nerakstitieVardirep[a - 1]

        b = int(len(varduNozimesVardi))
        varduNozimesVardi.pop()
        vardiFinalKopa = []
        for row in varduNozimesVardi:
            vardiFinal = row.text
            vardiFinalKopa.append(vardiFinal) # Vardi kuriem trukst nozimes pashlaik
        
        
        nerakstitieVardukopa = []
        for spanVardi in nerakstitieVardi:
            nerakstitieVardukopa.append(spanVardi)

        rowVardi = []
        for nerakstitieVardukopaSpan in nerakstitieVardukopa: # Nerakstitie vardi kalendara beigas
            nerakstitieVardiFinal = nerakstitieVardukopaSpan.text
            rowVardi.append(nerakstitieVardiFinal)

        nerakstitieVardirep.pop() # Visi nerakstitie vardi tiek nonemti no saraksta
        
        repNozimes = []
        for row2 in nerakstitieVardirep:
            repNozimes.append(row2.text)
        
    
        varduKopa = []
        for i in range(len(nerakstitieVardirep)):
            varduKopa.append([vardiFinalKopa[i], repNozimes[i]])
            
        def vardiKopa():
            for i in range(len(varduKopa)):
                for j in range(len(varduKopa[i])):
                    print(varduKopa[i][j])
                atstarpe(1)

        def rowVardu():
            if len(rowVardi) != 0:
                print("Vārdi, kas nav iekļauti kalendārā:")
                for i in range(len(rowVardi)):
                    if i+1 == len(rowVardi):
                        print(rowVardi[i], end="")
                    else:
                        print(rowVardi[i]+",", end=" ")  
            else:
                print("")

        
        print("\r" + " " * 20, end="")
        atstarpe(1)
        print("#" * 190)
        atstarpe(1)

        print(vardaDiena) # Varda diena un datums
        atstarpe(2)
        
        vardiKopa() # Vardi un to nozimes
        atstarpe(2)

        rowVardu() # Nerakstitie vardi
        atstarpe(2)
        print("#" * 190)
        

else:
    print("Kļūda, vārds ir nepareizi uzrakstīts vai arī nav atzīmēts kalendārā")
    exit()


input()