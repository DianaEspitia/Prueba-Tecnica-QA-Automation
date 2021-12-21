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
driver.get('https://www.amazon.com/') #Abrir página de Amazon

#Búsqueda de artículo
barra = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]') 
barra.send_keys('consola de videojuegos')
barra.send_keys(Keys.ENTER)

#Espera 
wait = WebDriverWait(driver,10)
bandera = '//*[@id="deliveryRefinements"]'

try:
    espera = wait.until(ec.visibility_of_element_located((By.XPATH, bandera)))
except Exception as e:
    print("Fallas en la prueba, el elemento indicado (bandera) no fue encontrado.")
    print()
    print(str(e))
    exit()

#Elección de artículo    
try:
    articulo = driver.find_element(By.CLASS_NAME, 's-image')
    if articulo is not None:
        articulo.click()
except Exception as e2:
    print("Fallas en la prueba, el articulo indicado no fue encontrado.")
    print()
    print(str(e2))
    exit()
    
#Esperar a que se encuentre el botón para agregar el carrito de compras
try:
    boton_agregar_carrito = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]'))) 
    agregar = driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]') #Agregar artículo al carrito de compras
    if agregar is not None:
        agregar.click()
except Exception as e3:
    print("Fallas en la prueba. El botón para agregar el artículo al carrito de compras no se encontró, esto puede ser porque el producto seleccionado no se encuentra disponible.")
    print()
    print(str(e3))
    exit()

#Ver carrito
carrito = driver.find_element(By.XPATH, '//*[@id="nav-cart"]')
if carrito is not None:
    carrito.click()

##Checkout
try:
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input'))) 
    proceder_pago = driver.find_element(By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input')
    if proceder_pago is not None:
        proceder_pago.click()
except Exception as e3:
    print("Fallas en la prueba. El botón para proceder con el pago no se encontró, esto puede ser porque el producto seleccionado no se encuentra disponible.")
    print()
    print(str(e3))
    exit()

print("La prueba se ha completado con éxito")

driver.close()


