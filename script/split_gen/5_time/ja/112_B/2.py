def main():
    n, t = map(int, input().split())
    min_cost = 1001
    for i in range(n):
        c, tt = map(int, input().split())
        if tt <= t:
            if min_cost > c:
                min_cost = c
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)
