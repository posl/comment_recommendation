def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    n = len(a)
    if a[0] > w:
        print(0)
        return
    if a[0] + a[1] > w:
        print(1)
        return
    if a[0] + a[1] + a[2] > w:
        print(2)
        return
    print(3 + (w - a[0] - a[1] - a[2]) // a[0])
