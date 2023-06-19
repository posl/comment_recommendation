def main():
    N = int(input())
    S = input()
    S = list(S)
    for i in range(1, N-1, 2):
        if S[i] == ',':
            S[i] = '.'
    print(''.join(S))

if __name__ == '__main__':
    main()