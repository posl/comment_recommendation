def main():
    N, T = map(int, input().split())
    min_cost = T + 1
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T and c < min_cost:
            min_cost = c
    if min_cost == T + 1:
        print("TLE")
    else:
        print(min_cost)

if __name__ == '__main__':
    main()