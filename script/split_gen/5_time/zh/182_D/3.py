def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_x = 0
    x = 0
    for i in range(n):
        x += a[i]
        max_x = max(max_x, x)
    print(max_x)
