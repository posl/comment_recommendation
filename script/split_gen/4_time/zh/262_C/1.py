def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for j in range(1, N + 1):
        i = A[j - 1]
        if i >= j:
            continue
        if A[i - 1] == j:
            ans += 1
    print(ans)
