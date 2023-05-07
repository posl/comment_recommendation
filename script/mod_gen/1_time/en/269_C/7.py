def main():
    N = int(input())
    if N == 0:
        print(0)
        exit()
    bin_N = bin(N)[2:]
    bin_N = bin_N[::-1]
    num_1 = bin_N.count('1')
    for i in range(2**num_1):
        bin_i = bin(i)[2:].zfill(num_1)
        bin_i = bin_i[::-1]
        ans = 0
        for j in range(len(bin_N)):
            if bin_N[j] == '1':
                ans += 2**j * int(bin_i[0])
                bin_i = bin_i[1:]
        print(ans)

if __name__ == '__main__':
    main()