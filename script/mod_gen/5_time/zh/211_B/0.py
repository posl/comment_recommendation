def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    if 'H' in [S_1, S_2, S_3, S_4] and '2B' in [S_1, S_2, S_3, S_4] and '3B' in [S_1, S_2, S_3, S_4] and 'HR' in [S_1, S_2, S_3, S_4]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()