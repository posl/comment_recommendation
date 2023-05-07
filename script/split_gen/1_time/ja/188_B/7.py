def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #計算
    ans = 0
    for i in range(N):
        ans += A[i] * B[i]
    #出力
    if ans == 0:
        print("Yes")
    else:
        print("No")
