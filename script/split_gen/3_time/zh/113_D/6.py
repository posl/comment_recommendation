def amidakuji(H,W,K):
    ans = 0
    for i in range(1<<W-1):
        b = bin(i)[2:].zfill(W-1)
        flag = True
        for j in range(W-2):
            if b[j] == '1' and b[j+1] == '1':
                flag = False
        if flag == False:
            continue
        for j in range(W):
            if j == 0:
                now = j
            elif b[j-1] == '1':
                now += 1
            elif b[j-1] == '0':
                now -= 1
        if now == K-1:
            ans += 1
    return ans
H,W,K = map(int,input().split())
print(amidakuji(H,W,K)%1000000007)
