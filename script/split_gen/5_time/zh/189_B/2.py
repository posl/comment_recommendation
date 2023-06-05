def main():
    n, x = map(int, input().split())
    x *= 100
    sum = 0
    for i in range(n):
        v, p = map(int, input().split())
        sum += v * p
        if sum > x:
            print(i + 1)
            return
    print(-1)
