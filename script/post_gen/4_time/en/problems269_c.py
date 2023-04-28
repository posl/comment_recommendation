Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    N_bin = format(N, 'b')
    N_len = len(N_bin)
    N_list = []
    for i in range(N_len):
        if N_bin[i] == '1':
            N_list.append(i)
    #print(N_list)

    for i in range(2**len(N_list)):
        tmp_bin = format(i, 'b')
        tmp_len = len(tmp_bin)
        tmp_list = []
        for j in range(tmp_len):
            if tmp_bin[j] == '1':
                tmp_list.append(j)
        #print(tmp_list)
        if set(tmp_list) <= set(N_list):
            print(i)

=======
Suggestion 2

def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_bin_len = len(N_bin)
    N_bin_1_pos = [i for i, x in enumerate(N_bin) if x == '1']

    for i in range(2**len(N_bin_1_pos)):
        x_bin = bin(i)[2:]
        x_bin = '0'*(len(N_bin_1_pos) - len(x_bin)) + x_bin
        x_bin_1_pos = [i for i, x in enumerate(x_bin) if x == '1']
        if set(x_bin_1_pos).issubset(set(N_bin_1_pos)):
            x_bin = '0'*(N_bin_len - len(x_bin)) + x_bin
            print(int(x_bin, 2))

=======
Suggestion 3

def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_len = len(N_bin)
    N_1 = [i for i in range(N_len) if N_bin[i] == "1"]
    max_x = 2**len(N_1)
    for i in range(max_x):
        x_bin = bin(i)[2:]
        x_len = len(x_bin)
        x_1 = [i for i in range(x_len) if x_bin[i] == "1"]
        if set(x_1).issubset(N_1):
            print(i)

=======
Suggestion 4

def get_binary_rep(n):
    binary_rep = []
    while n > 0:
        binary_rep.append(n % 2)
        n = n // 2
    return binary_rep

=======
Suggestion 5

def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_bin = N_bin[::-1]
    N_bin = list(N_bin)
    N_bin = [int(i) for i in N_bin]
    N_bin = N_bin[::-1]
    ans = []
    for i in range(60):
        if N_bin[i] == 1:
            ans.append(2**i)
    ans.append(2**60)
    ans.sort()
    print(len(ans))
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    n = int(input())
    n_bit = bin(n)[2:]
    n_len = len(n_bit)
    n_1 = [i for i, x in enumerate(n_bit) if x == "1"]
    for i in range(2**len(n_1)):
        bit = bin(i)[2:]
        bit = "0"*(len(n_1)-len(bit)) + bit
        bit = bit[::-1]
        bit = list(bit)
        n_bit_tmp = list(n_bit)
        for j in range(len(n_1)):
            n_bit_tmp[n_1[j]] = bit[j]
        print(int("".join(n_bit_tmp),2))

=======
Suggestion 7

def solve(n):
    if n == 0:
        print(0)
        return
    print(0)
    for i in range(1, 60):
        if n & (1 << i):
            print(1 << i)
    print(n)

n = int(input())
solve(n)

=======
Suggestion 8

def main():
    n = int(input())
    #n = 576461302059761664
    #n = 11
    #n = 0
    #n = 1

    #print(bin(n))
    #print(bin(n)[2:])
    #print(len(bin(n)[2:]))
    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))

    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))

    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))

    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))

    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))

    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))

    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))

    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))

    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))
    #print('')

    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))
    #print('')

    #print(bin(n).count('1'))
    #print(bin(n).count('0'))
    #print(bin(n).count('1') + bin(n).count('0'))
    #print('')

    #

=======
Suggestion 9

def get_bin(n):
    return format(n, 'b')
