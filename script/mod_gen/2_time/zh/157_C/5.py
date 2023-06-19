def solve():
    N,M = map(int,input().split())
    s = [0]*M
    c = [0]*M
    for i in range(M):
        s[i],c[i] = map(int,input().split())
    #print(s,c)
    ans = -1
    for i in range(10**N):
        num = str(i).zfill(N)
        flag = True
        for j in range(M):
            if num[s[j]-1] != str(c[j]):
                flag = False
                break
        if flag:
            ans = i
            break
    print(ans)
    return 0

if __name__ == '__main__':
    solve()