def main():
    H = list(map(int, input().split()))
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, H[0]+1):
        for j in range(1, H[1]+1):
            for k in range(1, H[2]+1):
                if i + j + k == H[0] and i + j + k == H[1] and i + j + k == H[2]:
                    for l in range(1, W[0]+1):
                        for m in range(1, W[1]+1):
                            for n in range(1, W[2]+1):
                                if l + m + n == W[0] and l + m + n == W[1] and l + m + n == W[2]:
                                    if i + l == j + m and j + m == k + n and i + l == k + n:
                                        ans += 1
    print(ans)
