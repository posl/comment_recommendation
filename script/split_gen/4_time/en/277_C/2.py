def main():
    n = int(input())
    ladders = []
    for _ in range(n):
        a, b = map(int, input().split())
        ladders.append((a, b))
    ladders.sort(key=lambda x:x[0])
    max_floor = 0
    for a, b in ladders:
        if max_floor < a:
            max_floor = b
    print(max_floor)
