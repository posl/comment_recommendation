def f(a, b):
    if a%2 == 0:
        if b%2 == 0:
            return (b-a)//2%2
        else:
            return (b-a)//2%2^b
    else:
        if b%2 == 0:
            return (b-a)//2%2^a
        else:
            return (b-a)//2%2^a^b
a, b = map(int, input().split())
print(f(a, b))
