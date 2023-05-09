def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    path = []
    path.append(1)
    next = a[1]
    while next != 1:
        path.append(next)
        next = a[next]
    path.append(1)
    if k < len(path):
        print(path[k])
    else:
        k -= len(path) - 1
        k %= len(path) - 1
        print(path[k])
