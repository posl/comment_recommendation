def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    ans = max(ans, A[i]*P + A[j]*Q + A[k]*R + A[l]*(0))
    if ans == 0:
        print("No")
    else:
        print("Yes")
