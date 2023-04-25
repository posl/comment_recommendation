Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_len = len(N_bin)
    result = []
    for i in range(2**N_len):
        i_bin = bin(i)[2:]
        i_len = len(i_bin)
        if i_len > N_len:
            break
        if i_len < N_len:
            i_bin = '0'*(N_len-i_len) + i_bin
        for j in range(N_len):
            if i_bin[j] == '1' and N_bin[j] == '0':
                break
        else:
            result.append(i)
    print(*result, sep='\n')

=======
Suggestion 2

def main():
    n = int(input())
    n = bin(n)[2:]
    n = n[::-1]
    ans = []
    for i in range(len(n)):
        if n[i] == '1':
            ans.append(str(2**i))
    print('\n'.join(ans))

=======
Suggestion 3

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    for i in range(1 << 15):
        x = 0
        for j in range(15):
            if i & (1 << j):
                x += 2 ** j
        if x <= n:
            ans.append(x)
    ans.sort()
    print(*ans, sep="\n")

=======
Suggestion 4

def main():
    N = int(input())
    max_bit = 0
    for i in range(60):
        if N & (1 << i):
            max_bit = i
    ans = []
    for i in range(1 << (max_bit + 1)):
        if i & N == i:
            ans.append(i)
    print(*ans, sep='\n')

=======
Suggestion 5

def main():
    n = int(input())
    n_str = bin(n)[2:]
    n_len = len(n_str)
    n_one = n_str.count('1')
    for i in range(2**n_one):
        i_str = bin(i)[2:]
        i_len = len(i_str)
        if i_len < n_one:
            i_str = '0' * (n_one - i_len) + i_str
        i_list = list(i_str)
        j = 0
        for k in range(n_len):
            if n_str[k] == '1':
                i_list.insert(k, '1')
        i_str = ''.join(i_list)
        print(int(i_str, 2))

=======
Suggestion 6

def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_len = len(N_bin)
    #print(N_bin, N_len)

    for i in range(2**N_len):
        i_bin = bin(i)[2:]
        i_len = len(i_bin)
        #print(i_bin, i_len)
        if i_len > N_len:
            break
        if all([N_bin[N_len - 1 - j] == i_bin[i_len - 1 - j] for j in range(i_len) if i_bin[i_len - 1 - j] == '1']):
            print(i)

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(2**15):
        if N & i == i:
            print(i)

=======
Suggestion 8

def solve():
    N = int(input())
    i = 1
    while i <= N:
        if i & N == i:
            print(i)
        i *= 2

=======
Suggestion 9

def main():
    n = int(input())
    n = bin(n)[2:]
    n = n[::-1]
    n = n.split("1")
    for i in range(len(n)):
        if n[i] != "":
            n[i] = (2**i)
    n = list(map(str,n))
    print(len(n))
    print(" ".join(n))

=======
Suggestion 10

def main():
    n = int(input())
    if n == 0:
        print(0)
        return

    # 1の場所を配列に格納
    one_pos = []
    for i in range(60):
        if (n >> i) & 1:
            one_pos.append(i)

    # 1の場所の組み合わせをbit全探索
    for i in range(1 << len(one_pos)):
        x = 0
        for j in range(len(one_pos)):
            if (i >> j) & 1:
                x += 1 << one_pos[j]
        print(x)

main()
