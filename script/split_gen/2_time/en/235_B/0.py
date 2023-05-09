def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = H[0]
    for i in range(1, N):
        if H[i] >= maxH:
            maxH = H[i]
        else:
            continue
    print(maxH)
