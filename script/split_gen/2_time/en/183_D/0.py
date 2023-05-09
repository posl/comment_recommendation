def main():
    n, w = map(int, input().split())
    events = []
    for _ in range(n):
        s, t, p = map(int, input().split())
        events.append((s, p))
        events.append((t, -p))
    events.sort()
    water = 0
    for t, p in events:
        water += p
        if water > w:
            print("No")
            return
    print("Yes")
