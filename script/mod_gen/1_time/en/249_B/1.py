def main():
    S = input()
    if len(S) < 2:
        print('No')
        return
    if S.islower():
        print('No')
        return
    if S.isupper():
        print('No')
        return
    if len(set(S)) != len(S):
        print('No')
        return
    print('Yes')
    return

if __name__ == '__main__':
    main()