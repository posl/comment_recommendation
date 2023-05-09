def f(a,b):
    if a == b:
        return a
    if a == 0:
        return f(1,b)
    if a % 2 == 0:
        return f(a-1,b) ^ a
    return f(a-1,b) ^ b
a,b = map(int,input().split())
print(f(a,b))

if __name__ == '__main__':
    f()