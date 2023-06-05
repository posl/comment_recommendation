def main():
    S = input()
    T = 'x' * 100000
    if S in T:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()