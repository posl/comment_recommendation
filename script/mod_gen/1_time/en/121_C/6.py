def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for A, B in AB:
        if M > B:
            ans += A * B
            M -= B
        else:
            ans += A * M
            break
    print(ans)

if __name__ == '__main__':
    main()