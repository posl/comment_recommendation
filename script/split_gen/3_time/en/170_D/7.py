def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    maxA = A[0]
    div = [0] * (maxA + 1)
    for i in range(N):
        div[A[i]] += 1
    for i in range(2, maxA + 1):
        for j in range(i, maxA + 1, i):
            div[i] += div[j]
    ans = 0
    for i in range(N):
        if div[A[i]] == 1:
            ans += 1
    print(ans)
