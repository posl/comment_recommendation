def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        print(S[N-i-1])

if __name__ == '__main__':
    main()