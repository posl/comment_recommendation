def main():
    # 入力
    A, B = map(int, input().split())
    # 出力
    print(A / (A + B), B / (A + B))

if __name__ == '__main__':
    main()