def main():
    N = int(input())
    A = list(map(int,input().split()))
    S = [0]
    for i in range(N):
        S.append(S[i]+A[i])
    min_diff = 10**10
    for i in range(1,N-1):
        for j in range(i+1,N):
            min_diff = min(min_diff,abs(S[i]-S[0]-max(S[i]-S[0],S[j]-S[i],S[N]-S[j])))
    print(min_diff)
