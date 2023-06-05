def cal(a,b,c,d):
    if b<=c or d<=a:
        return 0
    elif c<=a and b<=d:
        return b-a
    elif a<=c and d<=b:
        return d-c
    elif a<=c and c<=b and b<=d:
        return b-c
    elif c<=a and a<=d and d<=b:
        return d-a

if __name__ == '__main__':
    cal()