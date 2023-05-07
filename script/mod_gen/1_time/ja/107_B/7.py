def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    #print(A)
    # まずは、行ごとに黒いマスがあるかどうかを調べる
    # 黒いマスがある場合、その行は出力対象とする
    # なお、黒いマスがない場合は、その行は出力対象にしない
    for i in range(H):
        if '#' in A[i]:
            print(A[i])

if __name__ == '__main__':
    main()