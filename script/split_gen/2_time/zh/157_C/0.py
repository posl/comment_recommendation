def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    #print(N, M, s, c)
    num = []
    for i in range(N):
        num.append(-1)
    for i in range(M):
        num[s[i]-1] = c[i]
    #print(num)
    if num[0] == 0 and N != 1:
        print(-1)
    else:
        for i in range(N):
            if num[i] == -1:
                num[i] = 0
        #print(num)
        ans = 0
        for i in range(N):
            ans += num[i] * (10**(N-i-1))
        print(ans)
