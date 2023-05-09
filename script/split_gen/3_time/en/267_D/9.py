def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i, a in enumerate(A):
        ans += (i+1) * a
    ans -= sum(A[M:])
    print(ans)
