def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = []
    for L, R in LR:
        if ans:
            if ans[-1][1] >= R:
                continue
            elif ans[-1][1] >= L:
                ans[-1][1] = R
            else:
                ans.append([L, R])
        else:
            ans.append([L, R])
    for a in ans:
        print(*a)
