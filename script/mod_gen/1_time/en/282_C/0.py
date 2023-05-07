def main():
    N = int(input())
    S = input()
    for i in range(len(S)):
        if S[i] == ',' and i % 2 == 1:
            print('.', end='')
        else:
            print(S[i], end='')

if __name__ == '__main__':
    main()