def main():
    n, t = map(int, input().split())
    c = []
    for _ in range(n):
        c_i, t_i = map(int, input().split())
        if t_i <= t:
            c.append(c_i)
    if c:
        print(min(c))
    else:
        print("TLE")
