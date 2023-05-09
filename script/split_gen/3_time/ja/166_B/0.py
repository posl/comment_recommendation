def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    
    #print(N, K)
    #print(d)
    #print(A)
    
    # いたずらを受ける人数
    cnt = 0
    
    for i in range(N):
        # すぬけ君 i がいたずらを受けるかどうかのフラグ
        flag = 0
        
        for j in range(K):
            if (i+1) in A[j]:
                flag = 1
                break
        
        if flag == 0:
            cnt += 1
    
    print(cnt)
