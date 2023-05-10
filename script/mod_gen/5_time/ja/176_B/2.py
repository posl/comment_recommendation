def main():
    n = input()
    n_list = list(n)
    n_list = list(map(int, n_list))
    sum_n = sum(n_list)
    if sum_n % 9 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()