def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i]] = i
    ans = 0
    right = 0
    for i in range(N):
        if Q[i] > right:
            ans += 1
        right = Q[i]
    print(ans)
