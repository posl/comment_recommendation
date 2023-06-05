def main():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if (A[i]+A[j])%D == 0:
                count += 1
    if count >= K:
        print(D)
    else:
        print(-1)
