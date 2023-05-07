def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    for i in range(1 << (H * W)):
        cnt = 0
        for j in range(H * W):
            if i >> j & 1:
                cnt += 1
        if cnt != A + B:
            continue
        row = [0] * W
        for j in range(H * W):
            if i >> j & 1:
                row[j % W] += 1
        if max(row) > B:
            continue
        col = [0] * H
        for j in range(H * W):
            if i >> j & 1:
                col[j // W] += 1
        if max(col) > A:
            continue
        ans += 1
    print(ans)
main()
I was able to solve the problem by myself, but I didn't like the code because it was not clear what I was doing.
So I looked at the editorial and found a better solution.

if __name__ == '__main__':
    main()