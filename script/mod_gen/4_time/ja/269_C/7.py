def main():
    n = int(input())
    n_len = len(bin(n))-2
    #print(n_len)
    for i in range(2**n_len):
        #print(bin(i)[2:])
        if (i & n) == i:
            print(i)

if __name__ == '__main__':
    main()