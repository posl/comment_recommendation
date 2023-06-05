def main():
    # 读入数据
    s1 = input()
    s2 = input()
    s3 = input()
    # 获取所有的不重复字符
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    chars = list(chars)
    # 生成所有数字的排列
    from itertools import permutations
    for p in permutations(range(10), len(chars)):
        # 构造映射表
        d = {c: p[i] for i, c in enumerate(chars)}
        # 首位不能为0
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        # 将字符串转换为数字
        n1 = sum([d[s] * 10 ** (len(s1) - i - 1) for i, s in enumerate(s1)])
        n2 = sum([d[s] * 10 ** (len(s2) - i - 1) for i, s in enumerate(s2)])
        n3 = sum([d[s] * 10 ** (len(s3) - i - 1) for i, s in enumerate(s3)])
        # 判断是否满足条件
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")

if __name__ == '__main__':
    main()