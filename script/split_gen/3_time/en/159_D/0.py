def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * (n + 1)
    for i in range(n):
        count[a[i]] += 1
    total = 0
    for i in range(n + 1):
        total += count[i] * (count[i] - 1) // 2
    for i in range(n):
        print(total - (count[a[i]] - 1))
