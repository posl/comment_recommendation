def main():
    n = int(input())
    t = []
    for i in range(n):
        a, p, x = map(int, input().split())
        t.append([a, p, x])
    t.sort()
    for i in range(n):
        if t[i][2] > 0:
            print(t[i][1])
            return
    print(-1)
    return
