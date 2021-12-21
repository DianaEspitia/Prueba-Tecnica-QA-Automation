from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# Seleccionar el navegador
print('Seleccione el navegador que desea utilizar')
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
barra.send_keys('consola de videojuegos')
barra.send_keys(Keys.ENTER)

#Espera 
wait = WebDriverWait(driver,10)
elemento_consola = '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[7]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img'

try:
    espera = wait.until(ec.visibility_of_element_located((By.XPATH, elemento_consola)))
except Exception as e:
    print("Fallas en la prueba, el elemento indicado no fue encontrado.")
    print()
    print(str(e))
    exit()

#Elección de artículo                                     
articulo = driver.find_element(By.XPATH, elemento_consola)
if articulo is not None:
    articulo.click()

#Esperar a que se encuentre el botón para agregar el carrito de compras
try:
    boton_agregar_carrito = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]'))) 
except Exception as e2:
    print("Fallas en la prueba. El botón para agregar el artículo al carrito de compras no se encontró, esto puede ser porque el producto seleccionado no se encuentra disponible.")
    print()
    print(str(e2))
    exit()

#Agregar artículo al carrito de compras
agregar = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]') 
if agregar is not None:
    agregar.click()

#Ver carrito
carrito = driver.find_element_by_xpath('//*[@id="nav-cart"]')
if carrito is not None:
    carrito.click()

print("La prueba se ha completado con éxito")

driver.close()
