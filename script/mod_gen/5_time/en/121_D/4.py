def f(a,b):
    if a%2 == 0:
        if b%2 == 0:
            if (b-a)%4 == 1:
                return 1
            else:
                return 0
        else:
            if (b-a)%4 == 1:
                return 1^b
            else:
                return 0^b
    else:
        if b%2 == 0:
            if (b-a)%4 == 1:
                return 1^a
            else:
                return 0^a
        else:
            if (b-a)%4 == 1:
                return a^b
            else:
                return 0^a^b
a,b = map(int,input().split())
print(f(a,b))

if __name__ == '__main__':
    f()