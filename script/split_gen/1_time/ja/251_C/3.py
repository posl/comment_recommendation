def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in d:
            d[s] = [t, i]
        else:
            if d[s][0] < t:
                d[s] = [t, i]
    d = sorted(d.items(), key=lambda x: x[1][1])
    print(d[0][1][1] + 1)
