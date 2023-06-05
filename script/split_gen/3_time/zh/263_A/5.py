def main():
    #input
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    #output
    if a == b and b == c:
        if d == e:
            print('Yes')
        else:
            print('No')
    elif a == b and b == d:
        if c == e:
            print('Yes')
        else:
            print('No')
    elif a == b and b == e:
        if c == d:
            print('Yes')
        else:
            print('No')
    elif a == c and c == d:
        if b == e:
            print('Yes')
        else:
            print('No')
    elif a == c and c == e:
        if b == d:
            print('Yes')
        else:
            print('No')
    elif a == d and d == e:
        if b == c:
            print('Yes')
        else:
            print('No')
    elif b == c and c == d:
        if a == e:
            print('Yes')
        else:
            print('No')
    elif b == c and c == e:
        if a == d:
            print('Yes')
        else:
            print('No')
    elif b == d and d == e:
        if a == c:
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
