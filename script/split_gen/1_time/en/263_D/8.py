def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print (A)
    ans = 0
    for i in range(N):
        if A[i] > R:
            ans += (N - i) * R
            break
        elif A[i] < L:
            ans += (N - i) * L
            break
        else:
            ans += A[i]
    print (ans)
