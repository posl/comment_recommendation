def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = []
    for _ in range(m):
        b, c = map(int, input().split())
        bc.append((b, c))
    bc.sort(key=lambda x: x[1], reverse=True)
    j = 0
    for b, c in bc:
        for _ in range(b):
            if j < n and a[j] < c:
                a[j] = c
                j += 1
            else:
                break
        else:
            continue
        break
    print(sum(a))
