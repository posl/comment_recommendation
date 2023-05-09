def main():
    # リスト形式で入力
    x, y, z = map(int, input().split())
    # リストを入れ替え
    x, y = y, x
    x, z = z, x
    print(x, y, z)

if __name__ == '__main__':
    main()