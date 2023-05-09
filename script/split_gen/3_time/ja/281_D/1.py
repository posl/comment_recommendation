def main():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    S = set()
    for i in range(N):
        for j in range(i+1,N):
            S.add(A[i]+A[j])
    S = sorted(list(S))
    for i in range(len(S)-1,-1,-1):
        if S[i] % D == 0:
            print(S[i])
            return
    print(-1)
