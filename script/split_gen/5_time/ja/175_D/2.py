def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    C = list(map(int,input().split()))
    ans = -float('inf')
    for i in range(N):
        #print(i)
        tmp = 0
        t = 0
        j = i
        while True:
            #print(j)
            tmp += C[j]
            j = P[j]-1
            t += 1
            if j == i:
                break
            if t == K:
                break
        #print(tmp)
        if t == K:
            ans = max(ans,tmp)
        else:
            if tmp > 0:
                if K % t == 0:
                    ans = max(ans,tmp*(K//t))
                else:
                    ans = max(ans,tmp*(K//t)+max(0,tmp))
            else:
                ans = max(ans,tmp)
    print(ans)
