def main():
    # 入力
    M, H = map(int, input().split())
    # 処理
    if H % M == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()