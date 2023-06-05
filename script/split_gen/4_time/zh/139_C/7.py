def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(1, n):
        if h[i] <= h[i - 1]:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count
    print(max_count)
