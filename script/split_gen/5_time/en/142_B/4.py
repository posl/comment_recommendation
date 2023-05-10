def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if h[i] >= k:
            c += 1
    print(c)
