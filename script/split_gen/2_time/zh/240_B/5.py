def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    i = 0
    while i < n:
        count += 1
        while i + 1 < n and a[i] == a[i + 1]:
            i += 1
        i += 1
    print(count)
