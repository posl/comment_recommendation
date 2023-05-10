def main():
    a, n = map(int, input().split())
    if n % a == 0:
        print(0)
        return
    if a % 2 == 0 and n % 2 != 0:
        print(-1)
        return
    if a % 2 != 0 and n % 2 == 0:
        print(-1)
        return
    if a % 5 == 0 and n % 5 != 0:
        print(-1)
        return
    if a % 5 != 0 and n % 5 == 0:
        print(-1)
        return
    count = 1
    x = a
    while x % a != 0 or x < n:
        x = x * a
        count += 1
    print(count)
    return
