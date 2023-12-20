import sys
sys.path.insert(0, 'libs/sympy')

from sympy import symbols, integrate, latex

def calculator(funcao):


    f = formatFunction(funcao)
    symbol = 'x'

    x = symbols(symbol)

    result = integrate(f, x)
    format_result = latex(result)

    return {"result": format_result}

def formatFunction(funcao):
    funcao = funcao.replace("sen", "sin")
    funcao = funcao.replace("sexpn", "sin")
    funcao = funcao.replace("expxp", "exp")
    funcao = funcao.replace("eˆx", "exp(x)")
    funcao = funcao.replace("ˆ", "**")

    return funcao
