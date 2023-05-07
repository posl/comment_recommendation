def main():
    N = int(input())
    #Nを2進数に変換
    N_2 = bin(N)
    #Nの2進数表記の1の桁をリストに格納
    N_2_list = []
    for i in range(len(N_2)):
        if N_2[i] == "1":
            N_2_list.append(i)
    #Nの2進数表記の1の桁の数
    N_2_list_len = len(N_2_list)
    #Nの2進数表記の1の桁の数が0のとき
    if N_2_list_len == 0:
        print(0)
    #Nの2進数表記の1の桁の数が1以上のとき
    else:
        #Nの2進数表記の1の桁の数が1のとき
        if N_2_list_len == 1:
            print(0)
            print(2**(N_2_list[0]))
        #Nの2進数表記の1の桁の数が2以上のとき
        else:
            #Nの2進数表記の1の桁の数が2のとき
            if N_2_list_len == 2:
                print(0)
                print(2**(N_2_list[0]))
                print(2**(N_2_list[1]))
                print(2**(N_2_list[0])+2**(N_2_list[1]))
            #Nの2進数表記の1の桁の数が3以上のとき
            else:
                #Nの2進数表記の1の桁の数が3のとき
                if N_2_list_len == 3:
                    print(0)
                    print(2**(N_2_list[0]))
                    print(2**(N_2_list[1]))
                    print(2**(N_2_list[0])+2**(N_2_list[1]))
                    print(2**(N_2_list[2]))
                    print(2**(N_2_list[0])+2**(N_2_list[2]))
                    print(2**(N_2

if __name__ == '__main__':
    main()