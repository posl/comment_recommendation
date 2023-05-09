def main():
    n, m = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        s.append(k[i][1:])
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(m):
            count = 0
            for l in range(k[j][0]):
                if (i>>(s[j][l]-1)) & 1:
                    count += 1
            if count % 2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)
