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

if __name__ == '__main__':
    main()