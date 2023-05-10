def main():
    # 入力
    s, k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    # 文字列の長さ
    n = len(s)
    # 重複文字の数
    duplicate_count = 0
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count += 1
    # 重複文字の数を排除
    s = list(set(s))
    # 文字列の長さ
    n = len(s)
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count += 1
    # 重複文字の数を排除
    s = list(set(s))
    # 文字列の長さ
    n = len(s)
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count += 1
    # 重複文字の数を排除
    s = list(set(s))
    # 文字列の長さ
    n = len(s)
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count += 1
    # 重複文字の数を排除
    s = list(set(s))
    # 文字列の長さ
    n = len(s)
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count += 1
    # 重複文字の数を排除
    s = list(set(s))
    # 文字列の長さ
    n = len(s)
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count
