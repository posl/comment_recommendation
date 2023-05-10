def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input().rstrip()
    # input_lineを空白で分割して、input_lineに上書き
    N, M, X, Y = input_line.split()
    N = int(N)
    M = int(M)
    X = int(X)
    Y = int(Y)
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input().rstrip()
    # input_lineを空白で分割して、input_lineに上書き
    x = input_line.split()
    x = list(map(int, x))
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input().rstrip()
    # input_lineを空白で分割して、input_lineに上書き
    y = input_line.split()
    y = list(map(int, y))
    x.append(X)
    y.append(Y)
    x.sort()
    y.sort()
    if x[N] >= y[0]:
        print("War")
    else:
        print("No War")

if __name__ == '__main__':
    main()