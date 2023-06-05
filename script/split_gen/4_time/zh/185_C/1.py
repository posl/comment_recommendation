def f(l):
    if l==12:
        return 1
    else:
        return sum([f(l-i) for i in range(1,l-10)])
print(f(int(input())))
