def main():
    N, T = map(int, input().split())
    c = [0]*N
    t = [0]*N
    for i in range(N):
        c[i], t[i] = map(int, input().split())
    min_cost = 1001
    for i in range(N):
        if t[i] <= T:
            if c[i] < min_cost:
                min_cost = c[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)
