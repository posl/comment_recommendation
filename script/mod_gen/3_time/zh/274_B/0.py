def problems274_b():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    ans = [0] * w
    for i in range(w):
        for j in range(h):
            if a[j][i] == '#':
                ans[i] = 1
                break
    for i in range(w):
        if ans[i] == 1:
            for j in range(h):
                if a[j][i] == '#':
                    break
                else:
                    ans[i] += 1
    print(*ans)

if __name__ == '__main__':
    problems274_b()