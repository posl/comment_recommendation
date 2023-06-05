def main():
    n, w = map(int, input().split())
    events = []
    for i in range(n):
        s, t, p = map(int, input().split())
        events.append((s, p))
        events.append((t, -p))
    events.sort()
    current_water = 0
    for event in events:
        current_water += event[1]
        if current_water > w:
            print("No")
            return
    print("Yes")
