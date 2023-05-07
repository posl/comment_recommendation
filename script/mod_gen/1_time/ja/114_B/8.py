def main():
    # 1行目
    S = input()
    # 3文字ずつ取り出す
    S3 = [S[i:i+3] for i in range(len(S)-2)]
    # 3文字の差の絶対値を求める
    diff = [abs(int(s)-753) for s in S3]
    # 最小値を出力
    print(min(diff))

if __name__ == '__main__':
    main()