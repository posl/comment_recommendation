def main():
    a, b, c, d = map(int, input().split())
    if a > b * d:
        print(-1)
        return
    if c >= b and d > 1:
        print(-1)
        return
    if c < b:
        print(1)
        return
    count = 1
    while a > b * d:
        a += b
        a -= c
        count += 1
    print(count)
    return
