def main():
    H, W, A, B = map(int, input().split())
    HW = H * W
    ans = 0
    for i in range(2 ** HW):
        a = 0
        b = 0
        for j in range(HW):
            if (i >> j) & 1:
                a += 1
            else:
                b += 1
        if a == A and b == B:
            ans += 1
    print(ans)
