def main():
    N = int(input())
    s = [input() for i in range(N)]
    for i in range(N):
        print(s[N-1-i])

if __name__ == '__main__':
    main()