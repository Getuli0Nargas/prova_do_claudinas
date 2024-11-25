from codigo import Calculadora
#-------somar---------#
def somar(a, b):
        return a + b

def test_se_a_mais_b():
    assert somar (1,1) == 2
    assert somar (2,2) == 4

def test_somar_negativo():
    assert somar (-1, -1) == -2
    assert somar (-3,-7) == -10
#-------------------------------#

#-----------TESTE SUBTRAIR-------#
def subtrair(a, b):
    return a - b

def test_positivo_subtrair():
     assert subtrair(4,2) == 2
     assert subtrair(4,4) == 0

def test_negativo_subtrair():
     assert subtrair(-4,2) == -6
     assert subtrair(-10,4) == -14
#------------------#


#-----------TESTE SUBTRAIR-------#
def multiplicar(a, b):
    return a * b

def test_positivo_multiplicar():
     assert multiplicar(4,6) == 24
     assert multiplicar(4,5) == 20

def test_negativo_multiplicar():
     assert multiplicar(-6,2) == -12
     assert multiplicar(-3,2) == -6

#------------------#

#-----------TESTE SUBTRAIR-------#
def dividir(a, b):
    if b == 0:
         return "Erro: divisão por zero não permitida"
    return a / b

def test_positivo_dividir():
     assert dividir(4,2) == 2
     assert dividir(2,2) == 1

def test_negativo_dividir():
    assert dividir(-4,2) == -2
    assert dividir(-6,2) == -3
    
#------------------#