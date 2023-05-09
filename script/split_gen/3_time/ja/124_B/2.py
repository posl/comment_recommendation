def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(N):
        if max <= H[i]:
            count += 1
            max = H[i]
    print(count)
