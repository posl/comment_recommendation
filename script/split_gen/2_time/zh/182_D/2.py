def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    max_x = 0
    for i in range(n):
        x += a[i]
        if max_x < x:
            max_x = x
    print(max_x)
