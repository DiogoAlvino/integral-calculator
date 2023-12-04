from sympy import symbols, integrate

def calculator(funcao):

    f = funcao
    symbol = 'x'

    x = symbols(symbol)

    return {"result": integrate(f)}