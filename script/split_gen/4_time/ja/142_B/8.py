def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(0,n):
        if h[i] >= k:
            count += 1
    print(count)
