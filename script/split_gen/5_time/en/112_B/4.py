def main():
    n, t = map(int, input().split())
    c = 1001
    for i in range(n):
        ci, ti = map(int, input().split())
        if ti <= t:
            c = min(c, ci)
    if c == 1001:
        print("TLE")
    else:
        print(c)
