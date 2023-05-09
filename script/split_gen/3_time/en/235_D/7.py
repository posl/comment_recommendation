def main():
    a, n = map(int, input().split())
    if n % a == 0:
        print(-1)
        return
    x = 1
    i = 0
    while x != n:
        x = x * a
        if x % 10 == 0:
            x = x // 10
        else:
            x = x % 10
        i += 1
    print(i)
