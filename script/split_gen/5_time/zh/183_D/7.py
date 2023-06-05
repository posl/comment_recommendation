def main():
    n, w = map(int, input().split())
    events = []
    for i in range(n):
        s, t, p = map(int, input().split())
        events.append((s, p))
        events.append((t, -p))
    events.sort()
    water = 0
    for e in events:
        water += e[1]
        if water > w:
            print("No")
            return
    print("Yes")
