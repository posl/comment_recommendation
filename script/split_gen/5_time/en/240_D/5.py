def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n, a)
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    #print(d)
    count = 0
    for k, v in d.items():
        if v >= k:
            count += v - k
        else:
            count += v
    print(count)
