def main():
    import sys
    input = sys.stdin.readline
    def read_int():
        return int(input())
    def read_int_n():
        return list(map(int, input().split()))
    def read_int_n2(N):
        return [int(input()) for _ in range(N)]
    def read_int_n3(N):
        return [read_int_n() for _ in range(N)]
    def debug(*x):
        print(*x, file=sys.stderr)
    import math
    MOD = 998244353
    N = read_int()
    A = read_int_n()
    ans = [0]*10
    ans[A[0]] += 1
    for i in range(1,N):
        ans2 = [0]*10
        for j in range(10):
            ans2[(j+A[i])%10] += ans[j]
            ans2[(j*A[i])%10] += ans[j]
        for j in range(10):
            ans[j] = ans2[j]%MOD
    for i in range(10):
        print(ans[i])
main()
