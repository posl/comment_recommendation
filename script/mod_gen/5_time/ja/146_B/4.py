def main():
    N = int(input())
    S = input()
    for i in range(len(S)):
        if ord(S[i]) + N > 90:
            print(chr(ord(S[i]) + N - 26), end='')
        else:
            print(chr(ord(S[i]) + N), end='')

if __name__ == '__main__':
    main()