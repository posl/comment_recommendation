def main():
    N, T = map(int, input().split())
    min_cost = 1001
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T and c < min_cost:
            min_cost = c
    print(min_cost if min_cost < 1001 else "TLE")
main()

if __name__ == '__main__':
    main()