def func(a,b,c):
    if b >= a:
        return c - (b - a)
    else:
        return c
a,b,c = map(int, input().split())
print(func(a,b,c))

if __name__ == '__main__':
    func()