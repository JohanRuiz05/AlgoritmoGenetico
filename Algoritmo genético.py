import random
import time

# Crea el cromosoma inicial con 100 números binarios aleatorios de 6 genes

def cromosomas ():

    global cromosomaInicial
    
    cromosomaInicial = []

    for j in range (100):
        cromosomaInicial.append ([])
    
        for i in range (10):
                a = int (random.randint (0,1))
                cromosomaInicial[j].append (a)

    print (cromosomaInicial)
    print ()

    return cromosomaInicial

# Pasa cada uno de los cromosomas a un número decimal

def numeroBinario ():

    global cromosomaInicial
    global numero
    global listaTotal
    numero = 0
    listaTotal = []

    for i in range (100):
        nBinario = cromosomaInicial [i]

        for j in range (10):

            if (j == 9) and (nBinario [j] == 1):
                numero = numero + (2**0)
            else:
                pass
            if (j == 8) and (nBinario [j] == 1):
                numero = numero + (2**1)
            else:
                pass
            if (j == 7) and (nBinario [j] == 1):
                numero = numero + (2**2)
            else:
                pass
            if (j == 6) and (nBinario [j] == 1):
                numero = numero + (2**3)
            else:
                pass
            if (j == 5) and (nBinario [j] == 1):
                numero = numero + (2**4)
            else:
                pass
            if (j == 4) and (nBinario [j] == 1):
                numero = numero + (2**5)
            else:
                pass
            if (j == 3) and (nBinario [j] == 1):
                numero = numero + (2**6)
            else:
                pass
            if (j == 2) and (nBinario [j] == 1):
                numero = numero + (2**7)
            else:
                pass
            if (j == 1) and (nBinario [j] == 1):
                numero = numero + (2**8)
            else:
                pass
            if (j == 0) and (nBinario [j] == 1):
                numero = numero + (2**9)
            else:
                pass

        listaTotal.append (numero)
        numero = 0

    return listaTotal

# Tranforma cada número dentro del intervalo [0.5, 1], es decir x

def xIntervalo ():

    global listaTotal
    global listaX
    x = 0
    listaX = []
    
    for i in range (100):
        numTransformar = listaTotal[i]
        x = 0.5 + ((numTransformar/1023)*0.5)
        listaX.append ("{:.4f}".format(x))

# Se reemplaza x en la ecuación (5x^5)-(3x^4)-(x^3)-(5x^2)-x-3

def funcion ():

    global listaX
    global valorFuncion
    valorFuncion = []
    
    for i in range (100):
        x = float (listaX [i])
        f = (5*(x**5))-(3*(x**4))-(x**3)-(5*(x**2))-x-3
        valorFuncion.append ("{:.4f}".format(x))

    return valorFuncion

# Se halla la función de aptitud de cada x, del algoritmo, y después se establecen las probabilidades de elección

def aptitud ():

    global valorFuncion
    global valorProbSeleccion
    global aptitudTotal
    valorAptitudIndividual = []
    aptitudTotal = 0
    listaApt = []
    valorProbSeleccion = []  
    
    for i in range (100):
        aptitudIndividual = 100 - abs (float(valorFuncion [i]))
        valorAptitudIndividual.append ("{:.4f}".format(aptitudIndividual))
        aptT = float (valorAptitudIndividual [i])
        listaApt.append (aptT)

    for j in range (100):
        aptT2 = listaApt[j]
        aptitudTotal += aptT2

    for k in range (100):
        probSeleccion = (listaApt[k])/(aptitudTotal)
        valorProbSeleccion.append ("{:.10f}".format(probSeleccion))
        
    return valorProbSeleccion

# Se realiza la selección por clasificación

def seleccion ():

    global valorProbSeleccion
    global aptitudTotal
    global listaX
    global listaTotal
    global cromosomaInicial
    global cromosomaSeleccionado
    global nuevaAptitud
    global listaProbabilidades
    global seleccionClasificacion
    global valoresNuevaProb
    valorProbSeleccion.sort()
    valorProbSeleccion.reverse()
    
    contador1 = 100
    nuevaAptitud = {}
    
    for i in range (100):
        seleccion = valorProbSeleccion [i]
        nuevaAptitud [contador1] = seleccion
        contador1 -= 1

    valoresNuevaProb = list (nuevaAptitud.keys ())
    contador = 0
    listaProbabilidades = []
    nuevaProb1 = []
    nuevaProb2 = []
    nuevaProb3 = []
    nuevaProb4 = []
    nuevaProb5 = []
    
    while contador <= 19:
        nuevaProb1.append (valoresNuevaProb[contador])
        contador += 1
    while contador <= 39:
        nuevaProb2.append (valoresNuevaProb[contador])
        contador += 1
    while contador <= 59:
        nuevaProb3.append (valoresNuevaProb[contador])
        contador += 1
    while contador <= 79:
        nuevaProb4.append (valoresNuevaProb[contador])
        contador += 1
    while contador <= 99:
        nuevaProb5.append (valoresNuevaProb[contador])
        contador += 1

    for j in range (len (nuevaProb1)):
        numero1 = (float (nuevaProb1 [j])/190)
        listaProbabilidades.append ("{:.10f}".format(numero1))
    for j in range (len (nuevaProb2)):
        numero2 = (float (nuevaProb2 [j])/590)
        listaProbabilidades.append ("{:.10f}".format(numero2))
    for j in range (len (nuevaProb3)):
        numero3 = (float (nuevaProb3 [j])/990)
        listaProbabilidades.append ("{:.10f}".format(numero3))
    for j in range (len (nuevaProb4)):
        numero4 = (float (nuevaProb4 [j])/1390)
        listaProbabilidades.append ("{:.10f}".format(numero4))
    for j in range ((len (nuevaProb5))):
        numero5 = (float (nuevaProb5 [j])/1790)
        listaProbabilidades.append ("{:.10f}".format(numero5))

    b = float (random.random())
    b = "{:.10f}".format(b)

    for k in range (99):

        if listaProbabilidades [k] > b:
            seleccionClasificacion = listaProbabilidades [k]
        else:
            b = float (random.random())
            b = "{:.10f}".format(b)

    indice = listaProbabilidades.index (seleccionClasificacion)

    y = int (valoresNuevaProb [indice])
    seleccionadoP1 = (99 - y)+2
    seleccionadoP2 = float (valorProbSeleccion [100 - seleccionadoP1])
    seleccionadoP3 = seleccionadoP2*(aptitudTotal)
    seleccionadoP3 = float ("{:.4f}".format(seleccionadoP3))
    seleccionadoP4 = 100 - seleccionadoP3
    seleccionadoP4 = "{:.4f}".format(seleccionadoP4)
    seleccionadoP5 = listaX.index (seleccionadoP4)
    seleccionadoP6 = listaTotal [seleccionadoP5]

    numeroS = bin(seleccionadoP6)
    numeroS = format(seleccionadoP6, 'b')

    if len (numeroS) == 1:
        numeroS = "0"+"0"+"0"+"0"+"0"+"0"+"0"+"0"+"0"+numeroS
    if len (numeroS) == 2:
        numeroS = "0"+"0"+"0"+"0"+"0"+"0"+"0"+"0"+numeroS
    if len (numeroS) == 3:
        numeroS = "0"+"0"+"0"+"0"+"0"+"0"+"0"+numeroS
    if len (numeroS) == 4:
        numeroS = "0"+"0"+"0"+"0"+"0"+"0"+numeroS
    if len (numeroS) == 5:
        numeroS = "0"+"0"+"0"+"0"+"0"+numeroS
    if len (numeroS) == 6:
        numeroS = "0"+"0"+"0"+"0"+numeroS
    if len (numeroS) == 7:
        numeroS = "0"+"0"+"0"+numeroS
    if len (numeroS) == 8:
        numeroS = "0"+"0"+numeroS
    if len (numeroS) == 9:
        numeroS = "0"+numeroS

    numeroS = list (numeroS)
    
    for i in range (10):
        numeroSX = numeroS [i]
        numeroS [i] = int (numeroSX)

    cromosomaS = cromosomaInicial.index (numeroS)
    cromosomaSeleccionado = cromosomaInicial [cromosomaS]

    return nuevaAptitud
    return cromosomaSeleccionado

# Se corre el algoritmo genético para crear una nueva población y se realiza el cruce

def algoritmoGenetico():

    global cromosomaSeleccionado

    nuevaPoblacion = []

    cromosomas ()
    numeroBinario ()
    xIntervalo ()
    funcion ()
    aptitud ()
    seleccion ()

    for i in range (100):
        nuevaPoblacion.append (cromosomaSeleccionado)
        numeroBinario ()
        xIntervalo ()
        funcion ()
        aptitud ()
        seleccion ()

    for j in range (10):
        nCruce1 = random.randrange (1,100)
        nCruce2 = random.randrange (0,9)
        nCruce3 = random.randrange (1,100)
        nCruce4 = random.randrange (0,9)
        nuevaPoblacion [nCruce1][nCruce2] = nuevaPoblacion [nCruce3][nCruce4]

    print (nuevaPoblacion)
    print ()
    time.sleep(0.5)

# Se repite el algoritmo hasta que supere determinado umbral de aptitud

def funcionamiento ():

    algoritmoGenetico ()

    global aptitudTotal
    global valorProbSeleccion
    global nuevaAptitud

    prueba = 0
    
    while prueba < 200:
        algoritmoGenetico ()
        prueba += 1
        
    if prueba == 200:
        
        global aptitudTotal
        global listaX
        global listaTotal
        global cromosomaInicial
        global cromosomaSeleccionado
        global listaProbabilidades
        global seleccionClasificacion
        global valoresNuevaProb

        b = float (random.random())
        b = "{:.10f}".format(b)

        indice = listaProbabilidades.index (seleccionClasificacion)

        y = int (valoresNuevaProb [indice])
        seleccionadoP1 = (99 - y)+2
        seleccionadoP2 = float (valorProbSeleccion [100 - seleccionadoP1])
        seleccionadoP3 = seleccionadoP2*(aptitudTotal)
        seleccionadoP3 = float ("{:.4f}".format(seleccionadoP3))
        seleccionadoP4 = 100 - seleccionadoP3
        seleccionadoP4 = "{:.4f}".format(seleccionadoP4)
        seleccionadoP5 = listaX.index (seleccionadoP4)
        seleccionadoP6 = listaTotal [seleccionadoP5]

        numeroS = bin(seleccionadoP6)
        numeroS = format(seleccionadoP6, 'b')

        if len (numeroS) == 1:
            numeroS = "0"+"0"+"0"+"0"+"0"+"0"+"0"+"0"+"0"+numeroS
        if len (numeroS) == 2:
            numeroS = "0"+"0"+"0"+"0"+"0"+"0"+"0"+"0"+numeroS
        if len (numeroS) == 3:
            numeroS = "0"+"0"+"0"+"0"+"0"+"0"+"0"+numeroS
        if len (numeroS) == 4:
            numeroS = "0"+"0"+"0"+"0"+"0"+"0"+numeroS
        if len (numeroS) == 5:
            numeroS = "0"+"0"+"0"+"0"+"0"+numeroS
        if len (numeroS) == 6:
            numeroS = "0"+"0"+"0"+"0"+numeroS
        if len (numeroS) == 7:
            numeroS = "0"+"0"+"0"+numeroS
        if len (numeroS) == 8:
            numeroS = "0"+"0"+numeroS
        if len (numeroS) == 9:
            numeroS = "0"+numeroS

        numeroS = list (numeroS)
    
        for i in range (10):
            numeroSX = numeroS [i]
            numeroS [i] = int (numeroSX)

        cromosomaS = cromosomaInicial.index (numeroS)
        cromosomaSeleccionado = cromosomaInicial [cromosomaS]
        
        cromosomaSeleccionado = str (cromosomaSeleccionado)

        for j in range (10):
            cromosomaFinal = "".join(cromosomaSeleccionado)

        print ("El cromosoma " + cromosomaFinal + " posee la mejor aptitud para solucionar el problema.")
        print ()

funcionamiento ()
