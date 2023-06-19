def solve(s1, s2, s3):
    # 1. 从s1,s2,s3中提取出所有的字符
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        return 'UNSOLVABLE'
    chars = list(chars)
    # 2. 枚举所有可能的字符和数字的对应关系
    for perm in permutations(range(10), len(chars)):
        # 3. 利用这种对应关系，将s1,s2,s3转换为数字
        d = {c: p for c, p in zip(chars, perm)}
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = int(''.join(map(str, [d[c] for c in s1])))
        n2 = int(''.join(map(str, [d[c] for c in s2])))
        n3 = int(''.join(map(str, [d[c] for c in s3])))
        # 4. 判断是否满足等式
        if n1 + n2 == n3:
            return '\n'.join([str(n1), str(n2), str(n3)])
    return 'UNSOLVABLE'

if __name__ == '__main__':
    solve()