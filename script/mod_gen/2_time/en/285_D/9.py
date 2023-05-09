def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    # 2つのリストを結合して、重複を削除する
    # 重複がなければ、すべてのユーザーがその名前を使える
    # 重複があれば、その名前を使うユーザーが存在する
    if len(set(S+T)) == len(S+T):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()