def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort()
    ans = []
    for l, r in LR:
        if not ans or ans[-1][1] < l:
            ans.append([l, r])
        else:
            ans[-1][1] = max(ans[-1][1], r)
    for l, r in ans:
        print(l, r)
