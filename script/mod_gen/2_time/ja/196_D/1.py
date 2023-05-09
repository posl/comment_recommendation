def main():
    H, W, A, B = map(int, input().split())
    HW = H * W
    ans = 0
    for i in range(1 << HW):
        a = 0
        b = 0
        for j in range(HW):
            if (i >> j) & 1:
                if j % W < W - 1 and (i >> (j + 1)) & 1:
                    a += 1
                if j < HW - W and (i >> (j + W)) & 1:
                    b += 1
        if a == A and b == B:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()