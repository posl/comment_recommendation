def main():
    n = int(input())
    hi = list(map(int, input().split()))
    maxh = hi[0]
    for i in range(1,n):
        if hi[i] >= maxh:
            maxh = hi[i]
    print(maxh)
