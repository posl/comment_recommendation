def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 1
    for i in range(1, n):
        if a[i-1] != a[i]:
            count += 1
    print(count)
