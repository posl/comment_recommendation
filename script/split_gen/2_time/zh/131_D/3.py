def main():
    N = int(input())
    AB = []
    for _ in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))
    AB = sorted(AB, key=lambda x: x[1])
    now = 0
    for a, b in AB:
        now += a
        if now > b:
            print("No")
            return
    print("Yes")
