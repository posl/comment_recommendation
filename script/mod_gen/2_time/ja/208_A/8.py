def main():
    # A と B の入力
    A, B = map(int, input().split())
    # Yes / No の出力
    print("Yes" if (1 <= A and A <= 100) and (1 <= B and B <= 1000) and (A * 1 <= B and B <= A * 6) else "No")

if __name__ == '__main__':
    main()