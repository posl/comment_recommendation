def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    s = sum(A)
    T = T % s
    ans = 0
    t = 0
    for i in range(N):
        if t + A[i] > T:
            ans = i + 1
            break
        t += A[i]
    print(ans, t)
