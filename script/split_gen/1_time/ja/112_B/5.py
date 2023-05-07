def main():
    N, T = map(int, input().split())
    c = [0 for i in range(N)]
    t = [0 for i in range(N)]
    for i in range(N):
        c[i], t[i] = map(int, input().split())
    min_c = 1000000000
    for i in range(N):
        if t[i] <= T:
            if c[i] < min_c:
                min_c = c[i]
    if min_c == 1000000000:
        print("TLE")
    else:
        print(min_c)
