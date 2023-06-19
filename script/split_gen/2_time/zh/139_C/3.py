def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_count = 0
    count = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    print(max_count)
