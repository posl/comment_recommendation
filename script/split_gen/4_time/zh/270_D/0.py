def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.append(N+1)
    ans = 0
    for i in range(K):
        ans += max(0,A[i+1]-A[i]-1)
    print(N-ans)
