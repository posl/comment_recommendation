def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        if S[i-1] == '"' and S[i] == '"':
            print('.',end='')
        else:
            print(S[i-1],end='')
    print(S[N-1],end='')
    print()

if __name__ == '__main__':
    main()