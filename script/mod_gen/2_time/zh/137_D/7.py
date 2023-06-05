def main():
    N = int(input())
    strs = []
    for i in range(N):
        strs.append(input())
    strs.sort()
    cnt = 0
    ans = 0
    for i in range(N):
        if strs[i] == strs[i-1]:
            cnt += 1
        else:
            cnt = 0
        ans += cnt
    print(ans)

if __name__ == '__main__':
    main()