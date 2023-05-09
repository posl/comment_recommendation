def main():
    s1 = input()
    s2 = input()
    s3 = input()
    #print(s1,s2,s3)
    s1s2s3 = s1+s2+s3
    #print(s1s2s3)
    s1s2s3 = sorted(list(set(s1s2s3)))
    #print(s1s2s3)
    if len(s1s2s3) > 10:
        print('UNSOLVABLE')
        exit()
    for i in range(10):
        if str(i) in s1s2s3:
            continue
        else:
            s1s2s3.append(str(i))
    #print(s1s2s3)
    for i in range(10**len(s1s2s3)):
        num = str(i).zfill(len(s1s2s3))
        #print(num)
        num_dic = {}
        for j in range(len(s1s2s3)):
            num_dic[s1s2s3[j]] = num[j]
        #print(num_dic)
        n1 = ''
        n2 = ''
        n3 = ''
        for j in range(len(s1)):
            n1 += num_dic[s1[j]]
        for j in range(len(s2)):
            n2 += num_dic[s2[j]]
        for j in range(len(s3)):
            n3 += num_dic[s3[j]]
        if n1[0] == '0' or n2[0] == '0' or n3[0] == '0':
            continue
        if int(n1)+int(n2) == int(n3):
            print(int(n1))
            print(int(n2))
            print(int(n3))
            exit()
    print('UNSOLVABLE')
    return

if __name__ == '__main__':
    main()