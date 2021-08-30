
def sum_num(n, num=0):
    suma = 0
    while num <= n:
        suma = suma + num
        num += 1

    print(suma)


sum_num(5)

"""
formula mas eficiente
n=10
total=n*(n+1)//2 <- doble slash es para division entera
print total
"""

