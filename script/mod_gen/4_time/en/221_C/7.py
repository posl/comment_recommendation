def main():
    N = int(input())
    N_list = [int(x) for x in str(N)]
    N_list.sort(reverse=True)
    #print(N_list)
    N_list_len = len(N_list)
    N_list_1 = N_list[0:N_list_len//2]
    N_list_2 = N_list[N_list_len//2:N_list_len]
    #print(N_list_1)
    #print(N_list_2)
    N_list_1_num = 0
    N_list_2_num = 0
    for i in range(len(N_list_1)):
        N_list_1_num += N_list_1[i] * 10 ** i
    for i in range(len(N_list_2)):
        N_list_2_num += N_list_2[i] * 10 ** i
    #print(N_list_1_num)
    #print(N_list_2_num)
    print(N_list_1_num * N_list_2_num)

if __name__ == '__main__':
    main()