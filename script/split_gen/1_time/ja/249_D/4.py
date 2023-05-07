def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += A.count(A[i] * A[j])
    print(ans)
