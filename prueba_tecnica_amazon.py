from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# Seleccionar el navegador
print('Seleccione el buscador que desea utilizar')
print('1. Google Chrome')
print('2. Firefox')
print()
buscador = int(input('Buscador: '))

if buscador == 1:
    driver = webdriver.Chrome()
elif buscador == 2:
    driver = webdriver.Firefox()
else:
    print('Ingresó un valor incorrecto')
    exit()

driver.maximize_window()
driver.get('https://www.amazon.com/-/es/') #Abrir página de Amazon

#Búsqueda de artículo
barra = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]') 
barra.send_keys('Consola de videojuegos')
barra.send_keys(Keys.ENTER)

#Espera 
wait = WebDriverWait(driver,10)
elemento_consola = '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[9]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img'
articulo1 = wait.until(ec.visibility_of_element_located((By.XPATH, elemento_consola)))
if articulo1 is None:
    "El elemento no fue encontrado"
    exit()

#Elección de artículo                                     
articulo = driver.find_element(By.XPATH, elemento_consola)
if articulo is not None:
    articulo.click()

boton_agregar_carrito = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]'))) #Espera 
if boton_agregar_carrito is None:
    "El elemento no fue encontrado"
    exit()

#Agregar artículo al carrito de compras
agregar = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]') 
if agregar is not None:
    agregar.click()

#Ver carrito
carrito = driver.find_element_by_xpath('//*[@id="nav-cart"]')
if carrito is not None:
    carrito.click()

driver.close()

