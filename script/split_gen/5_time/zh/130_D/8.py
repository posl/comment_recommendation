def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    #print(A[2:4])
    cnt = 0
    for i in range(N):
        for j in range(i, N):
            #print(A[i:j+1])
            if sum(A[i:j+1]) >= K:
                cnt += 1
    print(cnt)
