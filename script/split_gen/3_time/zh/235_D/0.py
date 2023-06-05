def main():
    a, n = map(int, input().split())
    x = 1
    count = 0
    while x < n:
        if x % a == 0:
            x *= a
        else:
            x *= a
            x = int(str(x)[::-1])
        count += 1
    if x == n:
        print(count)
    else:
        print(-1)
