def main():
    S = input()
    if len(S) != 4:
        print('No')
        return
    if len(set(S)) == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()