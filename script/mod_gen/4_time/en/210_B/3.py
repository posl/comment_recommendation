def main():
    N = int(input())
    S = input()
    i = 0
    while i < N:
        if S[i] == '1':
            break
        i += 1
    if i % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()