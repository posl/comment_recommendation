def main():
    N = int(input())
    H = list(map(int,input().split()))
    maxH = 0
    for i in range(1,N):
        if H[i-1] < H[i]:
            H[i] = H[i-1]
        else:
            maxH = max(maxH,H[i-1])
    print(H[N-1] if maxH < H[N-1] else maxH)
