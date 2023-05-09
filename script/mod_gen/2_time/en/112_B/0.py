def main():
    N, T = map(int, input().split())
    c = [0] * N
    t = [0] * N
    for i in range(N):
        c[i], t[i] = map(int, input().split())
    min_c = 1000
    for i in range(N):
        if t[i] <= T and c[i] < min_c:
            min_c = c[i]
    if min_c == 1000:
        print("TLE")
    else:
        print(min_c)

if __name__ == '__main__':
    main()