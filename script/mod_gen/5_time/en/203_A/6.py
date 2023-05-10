def func(a,b,c):
    if a==b:
        return c
    elif a==c:
        return b
    elif b==c:
        return a
    else:
        return 0
a,b,c = map(int,input().split())
print(func(a,b,c))

if __name__ == '__main__':
    func()