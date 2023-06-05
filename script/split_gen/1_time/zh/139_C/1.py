def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(1, n):
        if h[i] <= h[i-1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    print(max_count)
