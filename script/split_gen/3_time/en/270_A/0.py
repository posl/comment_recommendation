def main():
    a,b = map(int, input().split())
    s = 0
    if a == 1:
        s += 300000
    elif a == 2:
        s += 200000
    elif a == 3:
        s += 100000
    if b == 1:
        s += 300000
    elif b == 2:
        s += 200000
    elif b == 3:
        s += 100000
    if a == 1 and b == 1:
        s += 400000
    print(s)
    return 0
