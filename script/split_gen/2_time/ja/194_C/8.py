def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    #処理
    ans = 0
    for i in range(1,N):
        ans += (N-i)*A[i]**2 - 2*A[i]*sum(A[:i]) + i*A[i]**2
    #出力
    print(ans)
