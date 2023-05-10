def func(a,b,x):
    if a+b > x:
        return 0
    if a*10+b*10 <= x:
        return 10**9
    if a*9+b*9 <= x:
        return 10**8
    if a*8+b*8 <= x:
        return 10**7
    if a*7+b*7 <= x:
        return 10**6
    if a*6+b*6 <= x:
        return 10**5
    if a*5+b*5 <= x:
        return 10**4
    if a*4+b*4 <= x:
        return 10**3
    if a*3+b*3 <= x:
        return 10**2
    if a*2+b*2 <= x:
        return 10**1
    if a+b <= x:
        return 10**0
    return 0
