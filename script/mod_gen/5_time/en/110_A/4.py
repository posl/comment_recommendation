def allowance(a,b,c):
    if a==b==c:
        return 111*a
    elif a==b or b==c or a==c:
        return 111*max(a,b,c)
    else:
        return 111*min(a,b,c)+100*max(a,b,c)

if __name__ == '__main__':
    allowance()