def main():
    N = int(input())
    # 平方数のリスト
    squares = []
    for i in range(1, int(N**0.5)+1):
        squares.append(i**2)
    # 組み合わせのリスト
    combination = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            combination.append(i*j)
    # 平方数のリストと組み合わせのリストの積を集合に変換し、要素数を出力
    print(len(set(squares) & set(combination)))

if __name__ == '__main__':
    main()