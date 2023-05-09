def main():
    S = input()
    S_set = set(S)
    if len(S_set) == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()