def main():
    N, T = map(int, input().split())
    c = [0] * N
    t = [0] * N
    for i in range(N):
        c[i], t[i] = map(int, input().split())
    cost = T + 1
    for i in range(N):
        if t[i] <= T and c[i] < cost:
            cost = c[i]
    if cost == T + 1:
        print("TLE")
    else:
        print(cost)

if __name__ == '__main__':
    main()