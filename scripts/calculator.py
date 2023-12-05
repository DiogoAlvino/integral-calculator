from sympy import symbols, integrate, latex

def calculator(funcao):

    f = funcao
    symbol = 'x'

    x = symbols(symbol)

    result = integrate(f, x)
    format_result = latex(result)

    return {"result": format_result}