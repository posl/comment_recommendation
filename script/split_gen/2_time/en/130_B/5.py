def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 1
    for i in range(n):
        d = d + l[i]
        if d <= x:
            count += 1
    print(count)
