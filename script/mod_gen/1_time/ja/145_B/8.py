def main():
    N = int(input())
    S = input()
    print('Yes' if S[:N//2] == S[N//2:] else 'No')

if __name__ == '__main__':
    main()