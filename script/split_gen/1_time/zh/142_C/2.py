def main():
    n = int(input())
    a = list(map(int, input().split()))
    r = []
    for i in range(n):
        r.insert(a[i] - 1, i + 1)
    print(' '.join(map(str, r)))
