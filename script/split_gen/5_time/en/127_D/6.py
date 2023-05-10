def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = []
    for _ in range(m):
        b,c = map(int, input().split())
        bc.append([b,c])
    a.sort()
    bc.sort(key=lambda x:x[1], reverse=True)
    i = 0
    for b,c in bc:
        for _ in range(b):
            if a[i] >= c:
                break
            a[i] = c
            i += 1
            if i == n:
                break
        if i == n:
            break
    print(sum(a))
