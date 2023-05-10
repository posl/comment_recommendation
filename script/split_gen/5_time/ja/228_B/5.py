def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    a.insert(0, 0)
    count = 0
    for i in range(1, n+1):
        if a[i] == x:
            count += 1
    print(count)
