import re
import pandas as pd
import os
import time
import pyautogui as pt
import tkinter as tk
from tkinter.simpledialog import askstring
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Busca = input("Busca: ")
# Crie uma instância de ChromeOptions para configurar as opções do navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# Crie o WebDriver com as opções configuradas
navegador = webdriver.Chrome(options=chrome_options)
# Endereço do Site
navegador.get("https://www.gov.br/pt-br")
time.sleep(2)
elemento = navegador.find_element(By.XPATH, '//*[@id="searchtext-input"]')  
elemento.click()
pt.write(Busca)
time.sleep(12)
pt.press('enter')
time.sleep(3)