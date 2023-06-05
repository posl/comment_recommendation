def main():
    # 读取输入
    x = raw_input()
    n = int(raw_input())
    s = []
    for i in range(n):
        s.append(raw_input())
    # 解决问题
    # 排序
    # 用一个字典来存储字母和新字母的映射
    x_dict = {}
    for i in range(26):
        x_dict[x[i]] = chr(ord('a')+i)
    # 用一个字典来存储新字母和字母的映射
    x_dict_reverse = {}
    for i in range(26):
        x_dict_reverse[chr(ord('a')+i)] = x[i]
    # 用一个字典来存储字符串和新字符串的映射
    s_dict = {}
    for i in range(n):
        s_dict[s[i]] = ''
        for j in range(len(s[i])):
            s_dict[s[i]] += x_dict[s[i][j]]
    # 排序
    s_dict_sorted = sorted(s_dict.items(), key=lambda d:d[1])
    # 输出
    for i in range(n):
        print s_dict_sorted[i][0]
