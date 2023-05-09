def main():
    n = int(input())
    # 2次元配列に格納
    name = [[input() for i in range(2)] for j in range(n)]
    # 2次元配列を1次元配列に変換
    name = [name[i][0] + name[i][1] for i in range(n)]
    # 重複を削除
    name = set(name)
    # 重複がある場合はYes, ない場合はNo
    if len(name) < n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()