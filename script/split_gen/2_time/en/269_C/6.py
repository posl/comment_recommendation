def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_bin = N_bin[::-1]
    N_bin = N_bin + "0"*(60-len(N_bin))
    N_bin = N_bin[::-1]
    N_bin = N_bin[2:]
    N_bin = N_bin[::-1]
    #print(N_bin)
    for i in range(2**60):
        i_bin = bin(i)[2:]
        i_bin = i_bin[::-1]
        i_bin = i_bin + "0"*(60-len(i_bin))
        i_bin = i_bin[::-1]
        i_bin = i_bin[2:]
        i_bin = i_bin[::-1]
        #print(i_bin)
        if len(i_bin) <= len(N_bin):
            if N_bin[:len(i_bin)] == i_bin:
                print(i)
        else:
            if i_bin == N_bin[:len(i_bin)]:
                print(i)
