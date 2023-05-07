def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == '0':
            if i % 2 == 0:
                print('Takahashi')
            else:
                print('Aoki')
            break

if __name__ == '__main__':
    main()