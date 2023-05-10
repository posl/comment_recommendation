def main():
    S = input()
    if (S.islower() == False) and (S.isupper() == False) and (len(S) == len(set(S))):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()