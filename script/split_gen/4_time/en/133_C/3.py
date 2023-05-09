def main():
    l, r = map(int, input().split())
    print(min(((i % 2019) * (j % 2019)) % 2019 for i in range(l, r + 1) for j in range(i + 1, r + 1)))
