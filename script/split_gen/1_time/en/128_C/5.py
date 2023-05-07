def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        s.append(k[i][1:])
        p.append(k[i][0])
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            count = 0
            for k in s[j]:
                if (i >> (k-1)) & 1:
                    count += 1
            if count % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
