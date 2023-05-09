def solve():
    s = input()
    mod = 10**9 + 7
    abc = [0, 0, 0]
    cnt = 0
    for c in s:
        if c == 'A':
            abc[0] += 1
        elif c == 'B':
            abc[1] += 1
        elif c == 'C':
            abc[2] += 1
        else:
            cnt += 1
    ans = 0
    for i in range(3**cnt):
        tmp = [0, 0, 0]
        for j in range(cnt):
            tmp[i % 3] += 1
            i //= 3
        if tmp[0] == 0 or tmp[1] == 0 or tmp[2] == 0:
            continue
        ans += abc[0] * abc[1] * abc[2]
        ans %= mod
        for j in range(3):
            abc[j] += tmp[j]
    print(ans)

if __name__ == '__main__':
    solve()