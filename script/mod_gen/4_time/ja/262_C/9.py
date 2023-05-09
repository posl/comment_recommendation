def solve():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if A[i] < i+1:
            continue
        for j in range(A[i], n+1):
            if j < A[j-1]:
                continue
            if A[i] == j and A[j-1] == i+1:
                ans += 1
            if j < A[i]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()