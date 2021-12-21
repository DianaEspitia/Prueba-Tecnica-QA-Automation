*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${Browser}      firefox
${Homepage}     https://www.amazon.com/
${barra_busqueda}       //*[@id="twotabsearchtextbox"]
${boton_busqueda}       //*[@id="nav-search-submit-button"]
${bandera}      //*[@id="deliveryRefinements"]
${articulo_consola}     s-image
${boton_agregar_carrito}    //*[@id="add-to-cart-button"]
${boton_ver_carrito}    //*[@id="nav-cart"]
${boton_proceder_pago}      //*[@id="sc-buy-box-ptc-button"]/span/input


*** Test Cases ***
AP001 Verificar que se puede agregar articulo al carrito de compras y hacer el checkout
    Open Browser    ${Homepage}     ${Browser}
    Maximize Browser Window
    Wait Until Element is Visible   xpath=${barra_busqueda}
    Input Text      xpath=${barra_busqueda}    consola de videojuegos
    Click Button    xpath=${boton_busqueda}
    Wait Until Element is Visible   xpath=${bandera}
    Wait Until Element is Visible   class=${articulo_consola}
    Click Element   class=${articulo_consola}
    Wait Until Element is Visible   xpath=${boton_agregar_carrito}
    Click Button    xpath=${boton_agregar_carrito}
    Wait Until Element is Visible   xpath=${boton_ver_carrito}
    Click Element    xpath=${boton_ver_carrito}
    Wait Until Element is Visible   xpath=${boton_proceder_pago}
    Click Button    xpath=${boton_proceder_pago}
    Close Browser
