def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(N):
        if max <= H[i]:
            max = H[i]
            count += 1
    print(max)
