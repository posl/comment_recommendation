def main():
    N = int(input())
    heights = list(map(int, input().split()))
    operations = 0
    for i in range(1, N):
        if heights[i] < heights[i-1]:
            operations += heights[i-1] - heights[i]
            heights[i] = heights[i-1]
    print(operations)
