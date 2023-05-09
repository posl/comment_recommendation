def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    ans = 0
    for i in range(2 ** n):
        bit = [0] * n
        for j in range(n):
            if (i >> j) & 1:
                bit[j] = 1
        flag = True
        for j in range(n):
            if bit[j] == 1:
                for k in range(1, a[j][0] + 1):
                    x = a[j][2 * k - 1] - 1
                    y = a[j][2 * k]
                    if bit[x] != y:
                        flag = False
        if flag:
            ans = max(ans, sum(bit))
    print(ans)
