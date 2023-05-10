def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    s1.reverse()
    s2.reverse()
    s3.reverse()
    s1_dict = {}
    s2_dict = {}
    s3_dict = {}
    for i in s1:
        s1_dict[i] = 0
    for i in s2:
        s2_dict[i] = 0
    for i in s3:
        s3_dict[i] = 0
    if len(s1_dict) > 10 or len(s2_dict) > 10 or len(s3_dict) > 10:
        print('UNSOLVABLE')
        return
    for i in range(10):
        if i in s1_dict.values():
            continue
        for j in range(10):
            if j in s2_dict.values():
                continue
            for k in range(10):
                if k in s3_dict.values():
                    continue
                if i == 0 and (s1[0] in s1_dict.keys() or s2[0] in s2_dict.keys() or s3[0] in s3_dict.keys()):
                    continue
                s1_dict[s1[0]] = i
                s2_dict[s2[0]] = j
                s3_dict[s3[0]] = k
                s1_num = 0
                s2_num = 0
                s3_num = 0
                for l in range(len(s1)):
                    s1_num += s1_dict[s1[l]] * (10 ** l)
                for l in range(len(s2)):
                    s2_num += s2_dict[s2[l]] * (10 ** l)
                for l in range(len(s3)):
                    s3_num += s3_dict[s3[l]] * (10 ** l)
                if s1_num + s2_num == s3_num:
                    print(s1_num)
                    print(s2_num)
                    print(s3_num)
                    return
                s1_dict[s1[0]] = 0
                s2_dict[s2[0]] = 0
                s3_dict[s3[0]] = 0
    print('UNSOLVABLE')

if __name__ == '__main__':
    main()