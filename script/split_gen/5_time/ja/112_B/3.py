def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    c = sorted(c, key=lambda x: x[0])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            return
    print("TLE")
