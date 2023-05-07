def main():
    S = [input() for _ in range(2)]
    if S[0][0] == S[0][1] == S[1][0] == S[1][1] == '.':
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()