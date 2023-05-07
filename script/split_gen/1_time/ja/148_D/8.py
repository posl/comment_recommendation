def main():
    N = int(input())
    A = list(map(int, input().split()))
    b = [0] * N
    for i in range(N):
        b[A[i] - 1] += 1
    ans = 0
    for i in range(N):
        if b[i] > i + 1:
            ans += b[i] - (i + 1)
    print(ans)
