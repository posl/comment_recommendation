def main():
    n, l = map(int, input().split())
    print(sum(range(l + 1, l + n)) - l if l >= 0 else sum(range(l + 1, l + n)) - l + 1)
