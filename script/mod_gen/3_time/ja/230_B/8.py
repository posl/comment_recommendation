def main():
    S = input()
    T = 'o' + 'x' * 10**5
    T = T + T
    if S in T:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()