def main():
    # 读入S_1,S_2,S_3
    s1 = input()
    s2 = input()
    s3 = input()
    # 生成字母表
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    # 生成S_1,S_2,S_3对应的数字
    char_to_num = {}
    for i, char in enumerate(chars):
        char_to_num[char] = i
    # 将S_1,S_2,S_3转换为数字
    n1 = 0
    for i, char in enumerate(s1):
        n1 += char_to_num[char] * pow(10, len(s1) - i - 1)
    n2 = 0
    for i, char in enumerate(s2):
        n2 += char_to_num[char] * pow(10, len(s2) - i - 1)
    n3 = 0
    for i, char in enumerate(s3):
        n3 += char_to_num[char] * pow(10, len(s3) - i - 1)
    # 求解
    for n_1 in range(pow(10, len(s1))):
        for n_2 in range(pow(10, len(s2))):
            if n_1 + n_2 == n3:
                if n1 == n_1 and n2 == n_2:
                    continue
                else:
                    print(n_1)
                    print(n_2)
                    print(n3)
                    return
    print("UNSOLVABLE")
