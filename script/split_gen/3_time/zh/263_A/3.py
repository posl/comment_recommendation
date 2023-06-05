def main():
    a,b,c,d,e = map(int,input().split())
    if a == b and b == c:
        if d == e:
            print('Yes')
        else:
            print('No')
    elif b == c and c == d:
        if a == e:
            print('Yes')
        else:
            print('No')
    elif c == d and d == e:
        if a == b:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
