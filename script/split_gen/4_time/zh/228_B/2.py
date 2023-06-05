def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    a = set(a)
    print(len(a))
