def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max_height = 0
    for i in range(N):
        if max_height <= H[i]:
            count += 1
            max_height = H[i]
    print(count)
