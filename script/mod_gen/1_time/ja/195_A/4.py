def main():
    #入力
    M, H = map(int, input().split())
    #出力
    print("Yes" if H % M == 0 else "No")

if __name__ == '__main__':
    main()