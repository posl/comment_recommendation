def main():
    N = int(input()) # N 回の操作を行う
    A = [0]*N # A_i 以上の整数を書く
    B = [0]*N # B_i 以下の整数を書く
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) // 2
    print(ans % (10**9 + 7))
