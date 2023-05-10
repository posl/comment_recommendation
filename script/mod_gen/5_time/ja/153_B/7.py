def main():
    # 標準入力受け取り
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # モンスターの体力を減らす
    for i in range(N):
        H -= A[i]
    # モンスターの体力が0以下ならYes
    if H <= 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()