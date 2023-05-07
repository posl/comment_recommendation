def main():
    input = sys.stdin.readline
    #入力
    P = list(map(int, input().split()))
    # 出力
    for i in range(26):
        print(chr(ord('a') + P[i] - 1), end = '')
