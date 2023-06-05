def burger(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + burger(n-1,1+(2**(n+1)-3)/2):
        return burger(n-1,x-1)
    elif x == 2 + burger(n-1,1+(2**(n+1)-3)/2):
        return 1 + burger(n-1,1+(2**(n+1)-3)/2)
    elif x <= 2 + 2*burger(n-1,1+(2**(n+1)-3)/2):
        return 1 + burger(n-1,x-2-burger(n-1,1+(2**(n+1)-3)/2))
    elif x == 3 + 2*burger(n-1,1+(2**(n+1)-3)/2):
        return 2 + burger(n-1,1+(2**(n+1)-3)/2)
    elif x <= 3 + 3*burger(n-1,1+(2**(n+1)-3)/2):
        return 2 + burger(n-1,x-3-burger(n-1,1+(2**(n+1)-3)/2))
    elif x == 4 + 3*burger(n-1,1+(2**(n+1)-3)/2):
        return 3 + burger(n-1,1+(2**(n+1)-3)/2)
    elif x <= 4 + 4*burger(n-1,1+(2**(n+1)-3)/2):
        return 3 + burger(n-1,x-4-burger(n-1,1+(2**(n+1)-3)/2))
    elif x == 5 + 4*burger(n-1,1+(2**(n+1)-3)/2):
        return 4 + burger(n-1,1+(2**(n+1)-3)/2)
    elif x <= 5 + 5*burger(n-1,1+(2**(n+1)-3)/2):
        return 4 + burger(n-1,x-5-burger(n-1,1+(2**(n+1)-3)/2))
    elif x == 6 + 5*burger(n-1,1+(
