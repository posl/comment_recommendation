def main():
    N, T = map(int, input().split())
    C = []
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            C.append(c)
    if len(C) == 0:
        print("TLE")
    else:
        print(min(C))
