def solve():
    n,m = map(int,input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    s.sort()
    ans = -1
    for i in range(3,n+1):
        for j in range(n-i+1):
            s2 = s[j:j+i]
            for k in range(2**i):
                s3 = []
                for l in range(i):
                    if k&(1<<l):
                        s3.append(s2[l])
                    else:
                        s3.append('_')
                s4 = s3[0]
                for l in range(1,i):
                    if s3[l] != '_' or s3[l-1] != '_':
                        s4 += s3[l]
                if s4 not in t:
                    ans = s4
    print(ans)

if __name__ == '__main__':
    solve()