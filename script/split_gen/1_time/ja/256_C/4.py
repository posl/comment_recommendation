def main():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    ans = 0
    for i in range(1, h[0] + 1):
        for j in range(1, h[1] + 1):
            for k in range(1, h[2] + 1):
                for l in range(1, w[0] + 1):
                    for m in range(1, w[1] + 1):
                        for n in range(1, w[2] + 1):
                            if i + j + k == h[0] and i + l + m == h[1] and i + n + k == h[2] and j + l + n == w[0] and j + m + k == w[1] and n + m + l == w[2]:
                                ans += 1
    print(ans)
