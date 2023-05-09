def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = []
    for l, r in LR:
        if ans and ans[-1][1] >= l:
            ans[-1][1] = max(ans[-1][1], r)
        else:
            ans.append([l, r])
    for l, r in ans:
        print(l, r)
main()

if __name__ == '__main__':
    main()