def main():
    N = int(input())
    S = input()
    if S[0:N//2] == S[N//2:N]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()