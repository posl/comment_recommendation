def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    total = 0
    for i in range(1, n+1):
        total += abs(a[i] - a[i-1])
    for i in range(1, n+1):
        print(total - abs(a[i] - a[i-1]) - abs(a[i] - a[i+1]) + abs(a[i-1] - a[i+1]))
