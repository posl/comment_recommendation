def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    s1_list = list(set(s1))
    s2_list = list(set(s2))
    s3_list = list(set(s3))
    if len(s1_list) > len(s3_list) or len(s2_list) > len(s3_list):
        print('UNSOLVABLE')
        return
    if len(s3_list) > 10:
        print('UNSOLVABLE')
        return
    for i in range(10**(len(s3_list)-1), 10**len(s3_list)):
        n1 = str(i)
        if len(n1) < len(s1_list):
            continue
        n1_list = list(n1)
        for j in range(len(s1_list)):
            if s1_list[j] in n1_list:
                n1_list.remove(s1_list[j])
            else:
                break
        else:
            n1 = int(n1)
            for k in range(10**(len(s3_list)-1), 10**len(s3_list)):
                n2 = str(k)
                if len(n2) < len(s2_list):
                    continue
                n2_list = list(n2)
                for l in range(len(s2_list)):
                    if s2_list[l] in n2_list:
                        n2_list.remove(s2_list[l])
                    else:
                        break
                else:
                    n2 = int(n2)
                    n3 = n1 + n2
                    if len(str(n3)) != len(s3_list):
                        continue
                    n3_list = list(str(n3))
                    for m in range(len(s3_list)):
                        if s3_list[m] in n3_list:
                            n3_list.remove(s3_list[m])
                        else:
                            break
                    else:
                        print(n1)
                        print(n2)
                        print(n3)
                        return
    else:
        print('UNSOLVABLE')
        return
