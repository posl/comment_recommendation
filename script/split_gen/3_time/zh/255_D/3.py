def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        count = 0
        for j in range(n):
            if a[j] >= x[i]:
                count += a[j] - x[i]
            else:
                count += n * (x[i] - a[j])
        print(count)
