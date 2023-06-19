def main():
    n, m = map(int, input().split())
    k = []
    for i in range(m):
        k.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    count = 0
    for i in range(2**n):
        switch = [0] * n
        for j in range(n):
            if ((i >> j) & 1):
                switch[j] = 1
        for j in range(m):
            sum = 0
            for l in range(1, k[j][0] + 1):
                sum += switch[k[j][l] - 1]
            if sum % 2 != p[j]:
                break
        else:
            count += 1
    print(count)
