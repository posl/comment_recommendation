def calc_prob(a,b,c,x):
    if x <= a:
        return 1
    elif a < x <= b:
        return c/(b-a)
    else:
        return 0
a,b,c,x = map(int,input().split())
print(calc_prob(a,b,c,x))
