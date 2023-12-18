from sympy import symbols, integrate, latex

def calculator(funcao):


    f = formatFunction(funcao)
    symbol = 'x'

    x = symbols(symbol)

    result = integrate(f, x)
    format_result = latex(result)

    return {"result": format_result}

def formatFunction(funcao):
    funcao = funcao.replace("ˆ", "**")
    funcao = funcao.replace("e", "exp")
    funcao = funcao.replace("sen", "sin")
    funcao = funcao.replace("sexpn", "sin")
    funcao = funcao.replace("expxp", "exp")

    return funcao
