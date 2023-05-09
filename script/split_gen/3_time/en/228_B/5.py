def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    count = 0
    used = [False] * n
    while not used[x]:
        used[x] = True
        x = a[x] - 1
        count += 1
    print(count)
