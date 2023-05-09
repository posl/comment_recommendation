def main():
    import sys
    N, M = map(int, input().split())
    if M == N - 1:
        for _ in range(M):
            u, v = map(int, input().split())
            if abs(u - v) > 1:
                print("No")
                sys.exit()
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()