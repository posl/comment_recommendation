def main():
    N,M = map(int,input().split())
    s = [None]*M
    for i in range(M):
        s[i] = list(map(int,input().split()))
    p = list(map(int,input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            count = 0
            for k in range(1,s[j][0]+1):
                if i & (1<<(s[j][k]-1)):
                    count += 1
            if count % 2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()