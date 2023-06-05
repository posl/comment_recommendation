def main():
    S = input()
    # print(S)
    S = list(S)
    S.sort()
    # print(S)
    print(''.join(S))
    # print(''.join(S).strip())

if __name__ == '__main__':
    main()