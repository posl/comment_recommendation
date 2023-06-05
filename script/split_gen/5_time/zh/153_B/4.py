def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(n):
        h -= a[i]
        if h <= 0:
            print('Yes')
            exit()
    print('No')
