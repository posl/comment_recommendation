def main():
    n, t = map(int, input().split())
    c = [0] * n
    time = [0] * n
    for i in range(n):
        c[i], time[i] = map(int, input().split())
    ans = 1001
    for i in range(n):
        if time[i] <= t:
            ans = min(ans, c[i])
    if ans == 1001:
        print('TLE')
    else:
        print(ans)
