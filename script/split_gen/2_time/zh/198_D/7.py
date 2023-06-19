def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        return
    if len(s3) > len(s1) + len(s2):
        return
    s1_set = set(s1)
    s2_set = set(s2)
    s3_set = set(s3)
    if len(s1_set) > 10 or len(s2_set) > 10 or len(s3_set) > 10:
        return
    if len(s1_set) + len(s2_set) > 10:
        return
    s_set = s1_set | s2_set | s3_set
    if len(s_set) > 10:
        return
    s_list = list(s_set)
    s_list.sort()
    s_map = {}
    for i in range(len(s_list)):
        s_map[s_list[i]] = i
    s1_num = 0
    s2_num = 0
    s3_num = 0
    for i in range(len(s1)):
        s1_num = s1_num * 10 + s_map[s1[i]]
    for i in range(len(s2)):
        s2_num = s2_num * 10 + s_map[s2[i]]
    for i in range(len(s3)):
        s3_num = s3_num * 10 + s_map[s3[i]]
    if s1_num + s2_num != s3_num:
        return
    if s1[0] == '0' or s2[0] == '0' or s3[0] == '0':
        return
    print(s1_num)
    print(s2_num)
    print(s3_num)
    return
