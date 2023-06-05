def main():
    s = input()
    k = int(input())
    # 算法
    # 1. 找出连续最长的X的长度
    # 2. 计算可以替换的X的个数
    # 3. 计算最终结果
    # 注意：当k大于等于可以替换的X的个数时，结果为字符串的长度
    #       当k小于可以替换的X的个数时，结果为连续最长的X的长度加上k
    # 1. 找出连续最长的X的长度
    max_x = 0
    tmp_max_x = 0
    for c in s:
        if c == 'X':
            tmp_max_x += 1
        else:
            max_x = max(max_x, tmp_max_x)
            tmp_max_x = 0
    max_x = max(max_x, tmp_max_x)
    # 2. 计算可以替换的X的个数
    count_x = 0
    for c in s:
        if c == 'X':
            count_x += 1
    replace_x = count_x - max_x
    # 3. 计算最终结果
    if replace_x <= k:
        print(len(s))
    else:
        print(max_x + k)
