def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    E = [list(map(int, input().split())) for i in range(M)]
    print(solve(N, M, E))

if __name__ == '__main__':
    main()