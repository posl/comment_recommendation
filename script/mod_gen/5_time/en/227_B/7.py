def main():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    if S[0] == S[1] and S[2] == S[3] and S[4] == S[5] and S[0] + S[2] == S[4]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()