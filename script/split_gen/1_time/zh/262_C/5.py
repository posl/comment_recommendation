def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] <= i + 1:
            continue
        for j in range(i + 1, n):
            if a[i] == j + 1 and a[j] == i + 1:
                count += 1
    print(count)
