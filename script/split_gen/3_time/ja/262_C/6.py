def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > i + 1:
            continue
        if i + 1 > A[A[i] - 1]:
            continue
        if i + 1 == A[A[i] - 1]:
            ans += 1
    print(ans)
