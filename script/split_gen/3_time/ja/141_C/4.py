def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    ans = [K - Q] * N
    for a in A:
        ans[a - 1] += 1
    for i in range(N):
        if ans[i] > 0:
            print("Yes")
        else:
            print("No")
