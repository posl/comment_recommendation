def amidakuji(H, W, K):
    #print(H, W, K)
    if W == 1:
        return 1
    #print('K',K)
    if K == 1:
        #print('K==1')
        return amidakuji(H-1, W-1, 1)
    if K == W:
        #print('K==W')
        return amidakuji(H-1, W-1, W-1)
    #print('K!=1&&K!=W')
    return amidakuji(H-1, W-1, K-1) + amidakuji(H-1, W-1, K) 
    
H, W, K = map(int, input().split())
print(amidakuji(H, W, K) % 1000000007)
