def main():
    n = int(input())
    height = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(1, n):
        if height[i] <= height[i - 1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    print(max(max_count, count))
