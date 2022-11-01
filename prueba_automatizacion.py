from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from collections import OrderedDict


wait_time =0
num_products=5
name_product=[]
producto=''
contador=0

def bot():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://amazon.com/")
    driver.implicitly_wait(5)

    wait_time=WebDriverWait(driver,30)
    #BUSQUEDA DE ZAPATILLAS ADIDADS
    wait_time.until(EC.element_to_be_clickable((By.ID,'twotabsearchtextbox')))\
                                    .send_keys(str("zapatillas adidas"))

    #CLICK EN EL BOTON DE BUSQUEDA
    wait_time.until(EC.element_to_be_clickable((By.ID,'nav-search-submit-button')))\
                                    .click()

    #MOSTRAR PRECIOS Y PRODUCTOS
    mostrar_cincoprod(wait_time=wait_time)
    
    #DESHABILITO EL FILTRO DE MARCA
    wait_time.until(EC.element_to_be_clickable((By.ID,'twotabsearchtextbox')))\
                                    .clear()
    wait_time.until(EC.element_to_be_clickable((By.ID,'twotabsearchtextbox')))\
                                    .send_keys(str("zapatillas"))

    #MOSTRAR PRECIOS Y PRODUCTOS
    mostrar_cincoprod(wait_time=wait_time)
    


def mostrar_cincoprod(wait_time):
    #MOSTRAR LOS 5 PRIMEROS NOMBRES DE LAS ZAPATILLAS
    nombre_zapatillas=wait_time.until(EC.presence_of_all_elements_located((By.XPATH,"//span[@class='a-size-base-plus a-color-base a-text-normal']")))
    zapatillas=[]
    for nombre in nombre_zapatillas:
        zapatillas.append(nombre.text)
    for i in range(0,5):
        print(zapatillas[i])

    #MOSTRAR LOS 5 PRIMERO PRECIOS DE LAS ZAPATILLAS
    precios=wait_time.until(EC.presence_of_all_elements_located((By.XPATH,"//span[@class='a-price-whole']")))
    vector_precios=[]
    for precio in precios:
        vector_precios.append(int(precio.text))
    for i in range(0,5):
        print(vector_precios[i])
    
    #ORDENAMOS POR EL PRECIO DE MAYOR A MENOR
    print("ordenamos precios: ")
    #print(sorted(vector_precios,reverse=True))

    #IMPRIMIMOS EL NOMBRE Y PRECIO DE LOS 5 PRIMEROS PRODUCTOS
    print("MOSTRAMOS LOS 5 PRIMEROS PRODUCTOS ORDENADOS POR EL PRECIO")
    productos=dict(zip(zapatillas,vector_precios))
    print(sorted(productos.items(), key=lambda t: t[1],reverse=True)[:5])
    

bot()