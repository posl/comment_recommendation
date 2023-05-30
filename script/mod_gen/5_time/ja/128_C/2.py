def main():
    N,M = map(int,input().split())
    k = []
    s = []
    for i in range(M):
        tmp = list(map(int,input().split()))
        k.append(tmp[0])
        s.append(tmp[1:])
    p = list(map(int,input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            tmp = 0
            for l in s[j]:
                if (i>>(l-1))&1:
                    tmp += 1
            if tmp%2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
main()
