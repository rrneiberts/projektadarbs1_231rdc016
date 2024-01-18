import selenium
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from tkinter import ttk
import time

url = "https://www.1188.lv/varda-dienas"
saturs = requests.get(url)
if saturs.status_code == 200:
    lapa = bs4.BeautifulSoup(saturs.content, "html.parser")
    atrada = lapa.find_all(class_="names")
    svin = atrada[0].string


def aiziet():
    vards = entry_Str.get()
    service = Service()
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)

    driver.get(url)
    time.sleep(1)

    find = driver.find_element(By.CLASS_NAME, "css-47sehv")
    find.click()

    find = driver.find_element(By.ID, "namedaysearch-nametext")
    find.send_keys(vards)
    time.sleep(0.5)
    find.send_keys(Keys.ENTER)

    url2 = driver.current_url

    if url != url2:
        find = driver.find_element(By.CLASS_NAME, "selected-date")
        vardaDiena = find.text

        saturs = requests.get(url2)

        if saturs.status_code == 200:
            lapa = bs4.BeautifulSoup(saturs.content, "html.parser")
            nerakstitieVardirep = lapa.find_all("p", class_=["content", "name"])
            varduNozimesVardi = lapa.find_all("h3", class_=["title", "content"])
            a = int(len(nerakstitieVardirep))
            nerakstitieVardi = nerakstitieVardirep[a - 1]

            b = int(len(varduNozimesVardi))
            varduNozimesVardi.pop()
            vardiFinalKopa = []
            for row in varduNozimesVardi:
                vardiFinal = row.text
                vardiFinalKopa.append(vardiFinal)

            nerakstitieVardukopa = []
            for spanVardi in nerakstitieVardi:
                nerakstitieVardukopa.append(spanVardi)

            rowVardi = []
            for nerakstitieVardukopaSpan in nerakstitieVardukopa:
                nerakstitieVardiFinal = nerakstitieVardukopaSpan.text
                rowVardi.append(nerakstitieVardiFinal)

            nerakstitieVardirep.pop()

            repNozimes = []
            for row2 in nerakstitieVardirep:
                repNozimes.append(row2.text)

            varduKopa = []
            for i in range(len(nerakstitieVardirep)):
                varduKopa.append([vardiFinalKopa[i], repNozimes[i]])

            output_label.config(text=vardaDiena)
            output_label2.config(text="")
            for i in range(len(varduKopa)):
                name_label = ttk.Label(master=window, text=f"{varduKopa[i][0]}:\n{varduKopa[i][1]}", font="Calibri 14", wraplength=680)
                name_label.pack(pady=5)

            output_label4 = ttk.Label(master=window, text="Kalendārā nerakstītie vārdi:", font="Calibri 14")
            output_label4.pack(pady=10, side="left")
            
            output_label3 = ttk.Label(master=window, text=rowVardi, font="Calibri 12", wraplength= 680)
            output_label3.pack(pady=10, side="left")

        else:
            print("Kļūda, vārds ir nepareizi uzrakstīts vai arī nav atzīmēts kalendārā")
            exit()


# window
window = tk.Tk()
window.title("Vārda dienas")
window.geometry("900x720")

# title
title_label = ttk.Label(master=window, text="Šodien vārda dienas svin " + svin, font="Calibri 24")
title_label.pack(pady=10)

# input field
input_frame = ttk.Frame(master=window)
entry_Str = tk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_Str)
button = ttk.Button(master=input_frame, text="Meklet", command=aiziet)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack()

# output field
output_label = ttk.Label(master=window, text="", font="Calibri 24")
output_label.pack(pady=10)

output_label2 = ttk.Label(master=window, text="", font="Calibri 14")
output_label2.pack(pady=10)



window.mainloop()
input()