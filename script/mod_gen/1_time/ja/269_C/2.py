def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_bin = [int(i) for i in N_bin]
    N_bin.reverse()
    for i in range(2**len(N_bin)):
        i_bin = bin(i)[2:]
        i_bin = [int(j) for j in i_bin]
        i_bin.reverse()
        if len(i_bin) < len(N_bin):
            i_bin = i_bin + [0]*(len(N_bin)-len(i_bin))
        flag = 0
        for j in range(len(N_bin)):
            if N_bin[j] == 1 and i_bin[j] == 0:
                flag = 1
                break
        if flag == 0:
            print(i)

if __name__ == '__main__':
    main()