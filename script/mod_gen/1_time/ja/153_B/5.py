def main():
    # 入力
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 処理
    if H <= sum(A):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()