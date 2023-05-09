def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 0
    for i in range(n):
        d = d + l[i]
        if d <= x:
            count = count + 1
        else:
            break
    if d <= x:
        count = count + 1
    print(count)
