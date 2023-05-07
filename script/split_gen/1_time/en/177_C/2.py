def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = 0
    for a in A:
        S -= a
        ans += a * S
    print(ans % (10**9 + 7))
