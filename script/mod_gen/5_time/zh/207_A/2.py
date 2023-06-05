def max_sum():
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a == b == c:
        print(a+b)
    elif a == b:
        print(a+c)
    elif a == c:
        print(a+b)
    elif b == c:
        print(b+a)
    else:
        print(max(a,b,c)*2)

if __name__ == '__main__':
    max_sum()