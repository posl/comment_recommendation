def arithmetic_sequence(a,b,c):
    if a==b and b==c:
        return True
    elif a==b or b==c or a==c:
        return False
    else:
        if a>b and a>c:
            if b>c:
                if a-b==b-c:
                    return True
                else:
                    return False
            else:
                if a-c==c-b:
                    return True
                else:
                    return False
        elif b>a and b>c:
            if a>c:
                if b-a==a-c:
                    return True
                else:
                    return False
            else:
                if b-c==c-a:
                    return True
                else:
                    return False
        elif c>a and c>b:
            if a>b:
                if c-a==a-b:
                    return True
                else:
                    return False
            else:
                if c-b==b-a:
                    return True
                else:
                    return False
a,b,c=map(int,input().split())

if __name__ == '__main__':
    arithmetic_sequence()