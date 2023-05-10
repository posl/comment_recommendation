def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = 1000000000
    for i in range(N):
        diff = abs(T - H[i] * 0.006 - A)
        if min_diff > diff:
            min_diff = diff
            ans = i + 1
    print(ans)
