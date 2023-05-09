def main():
    n, t = map(int, input().split())
    min_c = 1000
    for _ in range(n):
        c, time = map(int, input().split())
        if time <= t:
            min_c = min(min_c, c)
    if min_c == 1000:
        print("TLE")
    else:
        print(min_c)
