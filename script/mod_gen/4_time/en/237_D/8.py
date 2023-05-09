def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = input().rstrip()
    # 0を配列の中央に配置
    A = [0]
    # 1からNまでの数字を順番に追加
    for i in range(1, N + 1):
        # Lの場合は配列の先頭に追加
        if S[i - 1] == "L":
            A.insert(0, i)
        # Rの場合は配列の末尾に追加
        else:
            A.append(i)
    print(*A)

if __name__ == '__main__':
    main()