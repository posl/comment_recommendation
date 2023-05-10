def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i % 200 for i in a]
    b = []
    c = []
    for i in range(1, 2**min(n, 8)):
        sum = 0
        for j in range(min(n, 8)):
            if (i >> j) & 1:
                sum += a[j]
        sum %= 200
        if sum in b:
            c = []
            for j in range(min(n, 8)):
                if (i >> j) & 1:
                    c.append(j + 1)
            break
        else:
            b.append(sum)
    if c == []:
        print('No')
    else:
        print('Yes')
        print(len(b), *b)
        print(len(c), *c)
