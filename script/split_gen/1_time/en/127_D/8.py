def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = []
    for i in range(m):
        b, c = map(int, input().split())
        bc.append([b, c])
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        for _ in range(b):
            if i < n and c > a[i]:
                a[i] = c
                i += 1
            else:
                break
        if i >= n:
            break
    print(sum(a))
