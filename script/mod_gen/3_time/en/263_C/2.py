def print_sequences(N,M):
    if N==1:
        for i in range(1,M+1):
            print(i)
    else:
        for i in range(1,M+1):
            for sequence in print_sequences(N-1,M-i):
                print(i,*sequence)

if __name__ == '__main__':
    print_sequences()