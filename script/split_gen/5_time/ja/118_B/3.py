def main():
    n, m = map(int, input().split())
    a = [0] * m
    for i in range(n):
        k, *aa = map(int, input().split())
        for j in aa:
            a[j-1] += 1
    print(a.count(n))
