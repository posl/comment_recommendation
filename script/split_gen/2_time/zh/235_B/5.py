def main():
    n = int(input())
    h = list(map(int, input().split()))
    last = h[0]
    for i in range(1, n):
        if last < h[i]:
            last = h[i]
    print(last)
