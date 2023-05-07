def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    for i in range(1 << (H*W)):
        bit = i
        a = 0
        b = 0
        for j in range(H):
            for k in range(W):
                if bit & 1:
                    a += 1
                else:
                    b += 1
                bit >>= 1
            bit >>= W
        if a == A and b == B:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()