#Basico de red Neuronal
#ejemplo y teorias

#Para esto neccesitamos saber como funciona 
#Basicamente una red neuronal funcioina con las siguientes capas

#1. Una capa de valores, llamados inputs = En la primera capa
#esos valores vendran definidos por los datos de entrada, mientras que el 
#resto de capas recibiran el resultado de la capa anterior.

#2. Se realiza una suma ponderada todos los valores de entrada =
#Para hacer esa ponderacion necesitamos una matriz de pesos, como W.
#La matriz W tiene tantas filas como neuronas la capa anterior y tantas columnas 
#como neuronas tiene esa capa

#3 Al resultado de la suma ponderada anterior se le sumara otro parametro 
#conocido como bias o simpleente b = En este caso, cada neurona tiene su propio bias,
#por lo que las dimensiones del vector bias sera una colunma y tanatas filas como
#neuronas tiene esa capa

#4. Por cuarto lugar tenemos una de las claves de las redes neuronales: la funcion de
#activacion. Y es que, si te das cuenta, lo que tenemos hasta ahorra no es mas
#que una regresion lineal. Para evitar que toda la red neuronal se pueda reducir a una
#simple regresion lineal, al resultado de la suma del bias a la suma ponderada se le
#aplica una funcion, conocido como funcion de activacion. El resultado de esta
#funcion sera el resultado de la neurona.

#Por tanto, para poder montar una capa de una red neuronal solo necesitamos saber el 
#numero de neuronas en la capa y el numero de neuronas de la capa anterior.
#Con esto podremos crear tanto W como b.

#Para crear esta estructura vamos a crear una clase, que llamaremos capa. Ademas,
#vamos a inicializar los parametros (b y W) con datos aleatorios. Para esto ultimo
#usaremos la funcion "truconorm" de la libreria "stats", ya que nos permite crear datos
#aleatorios creando un rango, media y desviacion estandar, lo cual hara que nuestra red
#le cueste menos arrancar. In[1]

#Ejemplo:

from scipy import stats
import numpy as np
import math
import matplotlib.pyplot as plt

#Creamos las capas

class capa():

    def __init__(self, nNeuronasCapaAnterior,  nNeuronas, funcionAct):
        
        self.funcionAct = funcionAct
        
        self.b  = np.round(stats.truncnorm.rvs
        (-1, 1, loc=0, scale=1, size= nNeuronas).reshape(1,nNeuronas),3)
        
        self.W  = np.round(stats.truncnorm.rvs(
            -1, 1, loc=0, scale=1, size= nNeuronas * nNeuronasCapaAnterior).
            reshape(nNeuronasCapaAnterior, nNeuronas),3)

#Luego viene la activacion =
#El resultado del inpunt y el parametro bias se aplica una funcion de activacion

#Iniciamos con la funcion Sigmoide(con forma de S en el grafico)
#En esta funcion recie un valor x y devuelve un valor entre 0 y 1
#Esto hace que indique la probabilidad de un estado

#La funcion Sigmoide es uno de los tipos de activacion

sigmoide = (
  lambda x:1 / (1 + np.exp(-x)),
  lambda x:x * (1 - x)
  )

rango = np.linspace(-10,10).reshape([50,1])
datosSigmoide = sigmoide[0](rango)
datosSigmoideDerivada = sigmoide[1](rango)

#Cremos los graficos

fig, axes = plt.subplots(nrows=1, ncols=2, figsize =(15,5))
axes[0].plot(rango, datosSigmoide)
axes[1].plot(rango, datosSigmoideDerivada)
fig.tight_layout()

#Funcion  ReLu y es para valores negativos , esta funcion devuelve cero 0
#y para positivos devuelve el mismo valor. Esta funcion de activacion 
# es la mas usada en la redes neuronales

def derivadaReLu(x):
  x[x<=0] = 0
  x[x>0] = 1
  return x

relu = (
  lambda x: x * (x > 0),
  lambda x:derivadaReLu(x)
  )


datos_relu = relu[0](rango)
datos_relu_derivada = relu[1](rango)


# Volvemos a definir rango que ha sido cambiado
rango = np.linspace(-10,10).reshape([50,1])

# Cremos los graficos
plt.cla()
fig, axes = plt.subplots(nrows=1, ncols=2, figsize =(15,5))
axes[0].plot(rango, datos_relu[:,0])
axes[1].plot(rango, datos_relu_derivada[:,0])
plt.show()

#Ahora es tiempo de programar una red neuronal
#Para esto tendremos que indicar tres cosas
# - El numero decapas que tiene la red
# - El numero de neuronas en cada capa
# - La funcion de activacion que se usara en cada capas

#Con esto y con lo que se ha programado ya podemos crear la estructura de red neuronal

#Con esta red neuronal, la usaremos para solucionar un problema de clasificacion
#de dos clases, con la cual usaremos 4 capas 
#Una capa de entrada con dos neuronas, ya que usaremos dos variables
#Dos capas ocultas, una de 4 neuronas y otra de 8
# - Una capa de entrada con dos neuronas, ya que usaremos dos variables
# - Dos capas ocultas, una de 4neuronas y otra de 8.
# - Una capa de salida, con una unica neurona que predecira la clase.

#En este caso usaremos ReLu en todas las capas menos la ultima en la cual se usara una 
#funcion sigmoide. Hay que recordar que la primera capa solo se reciben los datos.

#Numero de neuronas en cada capa
#El primer valor es el numero de columnas de la capa de entrada

neuronas = [2, 4, 8, 1]

#Funciones de activacion usadas en cada capa

funcionesActivacion = [relu, relu, sigmoide]

#Con todo esto, ya podemos crear la estructura de nuestra red neuronal
#Lo haremos de forma iterativa e iremos guardando esta estructura en un nuevo objeto llamado
#redNeuronal

redNeuronal = []

for paso in range(len(neuronas)-1):
  x = capa(neuronas[paso], neuronas[paso + 1], funcionesActivacion[paso])
  redNeuronal.append(x)

print (redNeuronal)

#Con esto ya tenemos la estructura de nuestra red neuronal. Ahora solo quedarian dos pasos
#mas - por un lado conecta la red para que nos de una prediccion y un error, por el otro lado ir 
#propagando ese error hacia atras para ir entrenado a nuestra red neuronal.

#HACER QUE NUESTRA RED NEURONAL PREDIGA
#Hay que definir los calculos que tiene que seguir. los cuales son 3 los calculos a seguir:
# - Multiplicar los valores de entrada por la matriz de pesos W  sumar el parametro bias (b)
#y aplicar la funcion de activacion

#Luego hay que haceer una multiplicacion matricial

#Ejemplo de vector de entrada
X = np.round(np.random.randn(20, 2 ), 3)
z = X @ redNeuronal[0].W
print(z[:10, :], X.shape, z.shape)

#Ahora se suam el parametro bias (b) al resultado anterior

z = z + redNeuronal[0].b
print(z[:5, :])

#Ahora sigue la activacion de la capa

a = redNeuronal[0].funcionAct[0](z)
a[:5, :]

#Con esto tendriamos el resultado de la primera capa, que a su vez es
#la entrada para la segunda capa y asi hasta la ultima. Ahora podemos definir de forma iterativa
#dentro de un bucle

output = [X]

for numCapas in  range(len(redNeuronal)):
  z = output[-1] @ redNeuronal[numCapas].W + redNeuronal[numCapas].b
  a = redNeuronal[numCapas].funcionAct[0](z)
  output.append(a)

print(output[-1])

#Ya hecho esto es hora de entrenar nuestra red neuronal
#Para esto  hay que calcular cunato ha fallado. Para ello usaremos uno de los estimadores 
#mas tipicos en el mundo del machine learning - el error cuadratico medio (MSE)
#Calcular el error  cuadratico medio es algo bastante simple - a 