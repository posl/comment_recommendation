def main():
    n, x = map(int, input().split())
    for i in range(n):
        v, p = map(int, input().split())
        x -= v * p / 100
        if x < 0:
            print(i + 1)
            return
    print(-1)
    return
