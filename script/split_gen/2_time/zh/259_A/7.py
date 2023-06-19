def main():
    n, m, x, t, d = map(int, input().split())
    for i in range(1, n+1):
        if i == m:
            print(t)
            break
        if i < x:
            t += d
        else:
            t -= d
