def main():
    N = int(input())
    N_bin = bin(N)
    N_bin = N_bin[2:]
    N_bin = N_bin[::-1]
    for i in range(2**len(N_bin)):
        i_bin = bin(i)
        i_bin = i_bin[2:]
        i_bin = i_bin[::-1]
        flag = True
        for j in range(len(i_bin)):
            if i_bin[j] == '1':
                if j >= len(N_bin):
                    flag = False
                    break
                if N_bin[j] == '0':
                    flag = False
                    break
        if flag:
            print(i)

if __name__ == '__main__':
    main()