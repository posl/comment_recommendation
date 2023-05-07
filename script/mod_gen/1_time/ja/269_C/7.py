def main():
    N = int(input())
    #N = 0
    #N = 11
    #N = 576461302059761664
    N_binary = bin(N)[2:]
    N_binary_list = list(N_binary)
    N_binary_list.reverse()
    N_binary_list = [int(i) for i in N_binary_list]
    #print(N_binary_list)
    answer_list = []
    for i in range(2**len(N_binary_list)):
        i_binary = bin(i)[2:]
        i_binary_list = list(i_binary)
        i_binary_list.reverse()
        i_binary_list = [int(i) for i in i_binary_list]
        #print(i_binary_list)
        for j in range(len(i_binary_list)):
            if i_binary_list[j] == 1 and N_binary_list[j] == 0:
                break
            if j == len(i_binary_list)-1:
                answer_list.append(i)
    answer_list.sort()
    for i in answer_list:
        print(i)

if __name__ == '__main__':
    main()