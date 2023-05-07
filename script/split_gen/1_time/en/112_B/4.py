def main():
    n, t = map(int, input().split())
    cost = 1001
    for i in range(n):
        c, ti = map(int, input().split())
        if ti <= t:
            cost = min(cost, c)
    if cost == 1001:
        print('TLE')
    else:
        print(cost)
