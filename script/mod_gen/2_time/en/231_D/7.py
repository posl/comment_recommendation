def main():
    N, M = map(int, input().split())
    cond = [list(map(int, input().split())) for _ in range(M)]
    cond.sort(key=lambda x: x[1])
    ans = "Yes"
    for i in range(M):
        if i == 0:
            prev = cond[i][1]
            continue
        if cond[i][0] == prev:
            ans = "No"
            break
        prev = cond[i][1]
    print(ans)

if __name__ == '__main__':
    main()