def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            count = 0
            for l in range(k[j][0]):
                if (i >> (s[j][l] - 1)) & 1:
                    count += 1
            if count % 2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()