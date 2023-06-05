def main():
    a, b, c, d, e, f, x = map(int, input().split())
    taka = 0
    aoki = 0
    while True:
        if taka < x:
            taka = taka + a
        else:
            break
        if aoki < x:
            aoki = aoki + d
        else:
            break
        if taka < x:
            taka = taka + b
        else:
            break
        if aoki < x:
            aoki = aoki + e
        else:
            break
    if taka > aoki:
        print('高桥')
    elif taka < aoki:
        print('青木')
    else:
        print('画')
