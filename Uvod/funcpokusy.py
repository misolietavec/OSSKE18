def fib1(n):
    if n in [0,1]:
        return n
    p,a = 0,1
    for k in range(2,n+1):
        p,a = a,p+a
    return a

# Rekurzivna definicia
def fib2(n):
    if n in [0,1]:
        return n
    return fib2(n-1) + fib2(n-2)

def fact1(n):
    if n in [0,1]:
        return 1
    f = 1
    for k in range(2, n+1):
        f = f * k
    return f

# Rekurzivna definicia
def fact2(n):
    if n in [0,1]:
        return 1
    return n * fact2(n-1)
