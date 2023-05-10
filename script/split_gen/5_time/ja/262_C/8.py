def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= i + 1:
            continue
        for j in range(i + 1, A[i] + 1):
            if A[j - 1] <= i + 1:
                ans += 1
    print(ans)
main()
