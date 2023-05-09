def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    ans = 0
    for i in range(N - 1):
        if A[i] <= A[i + 1]:
            continue
        else:
            ans += A[i] - A[i + 1]
            A[i + 1] = A[i]
    print(ans)
