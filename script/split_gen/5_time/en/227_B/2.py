def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(n):
        if s[i] % 4 == 0:
            a += 1
        elif s[i] % 2 == 0:
            b += 1
        elif s[i] % 4 == 3:
            d += 1
        else:
            c += 1
    if c == 0:
        if a + 1 >= d:
            print('Yes')
        else:
            print('No')
    else:
        if a >= d:
            print('Yes')
        else:
            print('No')
