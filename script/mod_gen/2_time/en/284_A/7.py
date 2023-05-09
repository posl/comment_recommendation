def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        print(S[-i-1])

if __name__ == '__main__':
    main()