def solve(s1, s2, s3):
    # 重複文字を除いた文字リストを作成
    chars = list(set(s1 + s2 + s3))
    # 重複文字の数が10を超える場合は不正解
    if len(chars) > 10:
        return None
    # リストの先頭が0の場合は不正解
    if s1[0] in chars[0] or s2[0] in chars[0] or s3[0] in chars[0]:
        return None
    # 重複文字の数が10以下の場合は全探索
    for v in itertools.permutations(range(10), len(chars)):
        # マッピングテーブルを作成
        table = dict(zip(chars, v))
        # 先頭文字が0の場合は不正解
        if table[s1[0]] == 0 or table[s2[0]] == 0 or table[s3[0]] == 0:
            continue
        # 数値に変換
        n1 = int(''.join([str(table[s]) for s in s1]))
        n2 = int(''.join([str(table[s]) for s in s2]))
        n3 = int(''.join([str(table[s]) for s in s3]))
        # 覆面算の結果が正しい場合は正解
        if n1 + n2 == n3:
            return (n1, n2, n3)
    return None

if __name__ == '__main__':
    solve()