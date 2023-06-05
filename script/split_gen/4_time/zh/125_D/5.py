def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    minus = 0
    for i in range(N):
        ans += abs(A[i])
        if A[i] < 0:
            minus += 1
    if minus % 2 == 1:
        ans -= 2*min(abs(A))
    print(ans)
