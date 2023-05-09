def main():
    n, t = map(int, input().split())
    ct = [list(map(int, input().split())) for _ in range(n)]
    ct.sort(key=lambda x: x[0])
    for c, t_ in ct:
        if t_ <= t:
            print(c)
            exit()
    print("TLE")
