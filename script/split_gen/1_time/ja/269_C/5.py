def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_bin = N_bin[::-1]
    N_bin = list(N_bin)
    N_bin = [int(i) for i in N_bin]
    for i in range(2**len(N_bin)):
        i_bin = bin(i)[2:]
        i_bin = i_bin[::-1]
        i_bin = list(i_bin)
        i_bin = [int(i) for i in i_bin]
        if len(i_bin) < len(N_bin):
            i_bin = i_bin + [0 for i in range(len(N_bin) - len(i_bin))]
        flag = True
        for j in range(len(N_bin)):
            if i_bin[j] == 1:
                if N_bin[j] != 1:
                    flag = False
                    break
        if flag:
            print(i)
