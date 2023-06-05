def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_bin_list = []
    for i in range(len(N_bin)):
        if N_bin[i] == '1':
            N_bin_list.append(len(N_bin)-i-1)
    N_bin_list.reverse()
    #print(N_bin_list)
    ans = []
    for i in range(2**len(N_bin_list)):
        x_bin = bin(i)[2:]
        x_bin_list = []
        for j in range(len(x_bin)):
            if x_bin[j] == '1':
                x_bin_list.append(len(x_bin)-j-1)
        x_bin_list.reverse()
        #print(x_bin_list)
        if x_bin_list == []:
            ans.append(0)
        else:
            flag = True
            for j in x_bin_list:
                if j not in N_bin_list:
                    flag = False
                    break
            if flag:
                ans.append(i)
    for i in ans:
        print(i)
