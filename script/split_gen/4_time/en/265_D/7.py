def main():
    #input
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #compute
    A.sort()
    A.reverse()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if A[i] + A[j] + A[k] == P and A[j] + A[k] + A[l] == Q and A[k] + A[l] + A[i] == R:
                        ans += 1
    if ans > 0:
        print("Yes")
    else:
        print("No")
