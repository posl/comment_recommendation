def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    time = 0
    for a, b in AB:
        time += a + b
        if time > X:
            break
    else:
        print(time)
        return
    print(time - (time - X) // 2)
