def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #内積
    ans = 0
    for i in range(N):
        ans += A[i]*B[i]
    #出力
    if ans == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()