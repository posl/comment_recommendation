def main():
    #入力
    A, B = map(int, input().split())
    #A, B = 3, 4
    #A, B = 1, 0
    #A, B = 246, 402
    #処理
    X = A / (A**2 + B**2)**0.5
    Y = B / (A**2 + B**2)**0.5
    #出力
    print(X, Y)

if __name__ == '__main__':
    main()