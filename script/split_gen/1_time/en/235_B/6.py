def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    maxH = H[0]
    for i in range(1, N):
        if H[i] >= maxH:
            maxH = H[i]
    print(maxH)
