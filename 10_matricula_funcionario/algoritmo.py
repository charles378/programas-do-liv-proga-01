def somar (t, v):
    if v < 1500:
        salario = (t + v)/0.2
    else:
        salario = (t + v)/0.4
    return salario