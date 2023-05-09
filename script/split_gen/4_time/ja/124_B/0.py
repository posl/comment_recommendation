def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        if H[i-1] <= H[i]:
            count += 1
    print(count)
