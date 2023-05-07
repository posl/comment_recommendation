def main():
    l, r = map(int, input().split())
    l %= 2019
    r %= 2019
    if l >= r:
        print(0)
    elif l + 2019 <= r:
        print(0)
    else:
        print(min([i * j % 2019 for i in range(l, r) for j in range(i + 1, r + 1)]))
