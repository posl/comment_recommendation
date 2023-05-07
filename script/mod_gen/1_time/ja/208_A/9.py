def main():
    #入力
    A, B = map(int, input().split())
    #出力
    print("Yes" if A <= B <= A * 6 else "No")

if __name__ == '__main__':
    main()