def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    counter = 0
    for i in range(n):
        if h[i] >= k:
            counter += 1
    print(counter)
