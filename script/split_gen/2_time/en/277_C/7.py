def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    current = 1
    for a, b in AB:
        if current < a:
            current = a
        elif current < b:
            current = b
        else:
            print(1)
            return
    print(current)
