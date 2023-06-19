def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n-k):
        count += a[i]
    print(count)
