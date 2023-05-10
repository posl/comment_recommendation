def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s1_len = len(s1)
    s2_len = len(s2)
    s3_len = len(s3)
    if s1_len > 10 or s2_len > 10 or s3_len > 10:
        print("UNSOLVABLE")
        return
    s1_set = set(s1)
    s2_set = set(s2)
    s3_set = set(s3)
    if len(s1_set) > 10 or len(s2_set) > 10 or len(s3_set) > 10:
        print("UNSOLVABLE")
        return
    s_set = s1_set | s2_set | s3_set
    if len(s_set) > 10:
        print("UNSOLVABLE")
        return
    s_list = list(s_set)
    if len(s_list) == 1:
        if s1_len == 1 and s2_len == 1 and s3_len == 1:
            print(0)
            print(0)
            print(0)
            return
        else:
            print("UNSOLVABLE")
            return
    s_list.sort()
    s1_list = list(s1)
    s2_list = list(s2)
    s3_list = list(s3)
    s1_num = 0
    s2_num = 0
    s3_num = 0
    s1_num_list = []
    s2_num_list = []
    s3_num_list = []
    for i in range(s1_len):
        s1_num_list.append(0)
    for i in range(s2_len):
        s2_num_list.append(0)
    for i in range(s3_len):
        s3_num_list.append(0)
    for i in range(s1_len):
        for j in range(len(s_list)):
            if s1_list[i] == s_list[j]:
                s1_num_list[i] = j
                break
    for i in range(s2_len):
        for j in range(len(s_list)):
            if s2_list[i] == s_list[j]:
                s2_num_list[i] = j
                break
    for i in range(s3_len):
        for j in range(len(s_list)):
            if s3_list[i]
