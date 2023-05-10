def main():
    # 標準入力受け取り
    n = int(input())
    s = input()
    # 文字列を二回繰り返したものがあるかを判定
    if s[:n//2] == s[n//2:]:
        print('Yes')
    else:
        print('No')
