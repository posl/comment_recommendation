def main():
    n = int(input())
    s = input().split()
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(n):
        if int(s[i]) % 4 == 0:
            a += 1
        elif int(s[i]) % 2 == 0:
            b += 1
        elif int(s[i]) % 4 == 3:
            d += 1
        else:
            c += 1
    if d == 0:
        if a >= c - 1:
            print('Yes')
        else:
            print('No')
    else:
        if a >= c:
            print('Yes')
        else:
            print('No')
