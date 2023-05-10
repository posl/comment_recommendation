def f(a, b):
    if a == b:
        return a
    if a == 0:
        return f(a+1, b)
    if a % 2 == 0:
        return f(a+1, b) ^ a
    if b % 2 == 1:
        return f(a, b-1) ^ b
    return f(a+1, b) ^ a ^ f(1, b)
a, b = map(int, input().split())
print(f(a, b))

if __name__ == '__main__':
    f()