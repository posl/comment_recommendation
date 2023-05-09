def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        y = 0
        x = A[i]
        while x % 2 == 0:
            x //= 2
            y += 1
        if y <= M:
            M -= y
        else:
            ans += A[i]
    print(ans)
