def main():
    a, b, c, d, e, f, x = map(int, input().split())
    tak = 0
    aok = 0
    for i in range(1, x+1):
        if i % (a + b + c) <= a:
            tak += 1
        if i % (d + e + f) <= d:
            aok += 1
    if tak > aok:
        print('Takahashi')
    elif tak < aok:
        print('Aoki')
    else:
        print('Draw')
