def f(A, B, g):
    return (A / (g ** 0.5)) + B
A, B = map(int, input().split())
g = 1
while True:
    if f(A, B, g) >= f(A, B, g + 1):
        print(f(A, B, g))
        break
    else:
        g += 1
