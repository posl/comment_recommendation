def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    if len(s1) > len(s3) or len(s2) > len(s3):
        print('UNSOLVABLE')
        return
    for i in range(10 ** (len(s1) - 1), 10 ** len(s1)):
        for j in range(10 ** (len(s2) - 1), 10 ** len(s2)):
            if i + j > 10 ** len(s3):
                continue
            if len(str(i)) != len(s1) or len(str(j)) != len(s2):
                continue
            s1_flag = True
            s2_flag = True
            s3_flag = True
            for k in range(len(s1)):
                if s1[k] == s2[k] and str(i)[k] != str(j)[k]:
                    s1_flag = False
                    s2_flag = False
                if s1[k] == s3[k] and str(i)[k] != str(i + j)[k]:
                    s1_flag = False
                    s3_flag = False
                if s2[k] == s3[k] and str(j)[k] != str(i + j)[k]:
                    s2_flag = False
                    s3_flag = False
            if s1_flag and s2_flag and s3_flag:
                print(i)
                print(j)
                print(i + j)
                return
    print('UNSOLVABLE')

if __name__ == '__main__':
    main()