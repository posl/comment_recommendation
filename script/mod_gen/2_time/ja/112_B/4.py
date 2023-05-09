def main():
    N, T = map(int, input().split())
    min_cost = 1001
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T:
            min_cost = min(min_cost, c)
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

if __name__ == '__main__':
    main()