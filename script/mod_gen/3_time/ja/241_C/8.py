def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print("Yes" if check(N, S) else "No")

if __name__ == '__main__':
    main()