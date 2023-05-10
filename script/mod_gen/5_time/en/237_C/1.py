def main():
    S = input()
    if S == S[::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()