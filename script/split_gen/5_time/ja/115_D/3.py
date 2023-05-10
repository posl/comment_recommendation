def burger(n, x):
    if n == 0:
        return 1
    p = 2**(n+2)-3
    if x == 1:
        return 0
    elif x <= p:
        return burger(n-1, x-1)
    elif x == p+1:
        return 1+burger(n-1, x-1)
    elif x <= p*2:
        return 1+burger(n-1, x-1-p)+1
    else:
        return 1+burger(n-1, x-1-p*2)+1+burger(n-1, x-1-p*2)
n, x = map(int, input().split())
print(burger(n, x))
