def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        print(solve(S, t, k))

if __name__ == '__main__':
    main()