def main():
    n = int(input())
    h = list(map(int, input().split()))
    maxh = 0
    for i in range(n):
        if h[i] >= maxh:
            maxh = h[i]
    print(maxh)
