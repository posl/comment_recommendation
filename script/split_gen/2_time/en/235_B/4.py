def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = 0
    for i in range(N):
        if maxH <= H[i]:
            maxH = H[i]
    print(maxH)
