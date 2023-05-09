def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        print(S[N-1-i])

if __name__ == '__main__':
    main()