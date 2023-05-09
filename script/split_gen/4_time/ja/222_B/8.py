def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(n - a.count(p))
