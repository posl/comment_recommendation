def main():
    n, m = map(int, input().split())
    k = []
    s = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** n):
        flag = True
        for j in range(m):
            count = 0
            for x in range(1, k[j][0] + 1):
                if i & (1 << (s[j][x - 1] - 1)):
                    count += 1
            if count % 2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)
