def main():
    n = int(input())
    n_bin = bin(n)
    len_n = len(n_bin)
    n_bin = n_bin[2:len_n]
    n_bin = n_bin[::-1]
    #print(n_bin)
    #print(len(n_bin))
    n_list = []
    for i in range(len(n_bin)):
        if n_bin[i] == '1':
            n_list.append(i)
    #print(n_list)
    #print(len(n_list))
    ans = []
    for i in range(2**len(n_list)):
        i_bin = bin(i)
        len_i = len(i_bin)
        i_bin = i_bin[2:len_i]
        i_bin = i_bin[::-1]
        #print(i_bin)
        i_list = []
        for j in range(len(i_bin)):
            if i_bin[j] == '1':
                i_list.append(j)
        #print(i_list)
        #print(len(i_list))
        if i_list == []:
            ans.append(0)
        else:
            flag = 0
            for j in range(len(i_list)):
                if i_list[j] not in n_list:
                    flag = 1
                    break
            if flag == 0:
                ans.append(i)
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()