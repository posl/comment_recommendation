def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(a.index(min(a[n // 2:])) + 1)
