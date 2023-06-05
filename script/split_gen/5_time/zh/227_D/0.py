def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = sum(a[-k:])
    print(s)
