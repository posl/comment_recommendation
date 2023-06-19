def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    if S_1 == 'H' and S_2 == '2B' and S_3 == '3B' and S_4 == 'HR':
        print('Yes')
    elif S_1 == '2B' and S_2 == '3B' and S_3 == 'HR' and S_4 == '3B':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()