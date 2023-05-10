def main():
    N, K = map(int, input().split())
    for _ in range(N):
        P = list(map(int, input().split()))
        if sum(P) >= 3 * K:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()