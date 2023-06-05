def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    c.sort(key=lambda x: x[1])
    for i in range(n):
        if c[i][1] > t:
            c.pop(i)
            break
    if len(c) == 0:
        print("TLE")
    else:
        print(min(c, key=lambda x: x[0])[0])
