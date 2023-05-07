def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) + [i] for i in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.append([10**9, 10**9, 10**9])
    ans = 0
    cnt = 0
    prev = 0
    for i in range(N):
        if prev == AB[i][0]:
            cnt += 1
        else:
            cnt = 0
        ans += min(C, AB[i][1] - AB[i][0] + 1) * AB[i][2]
        prev = AB[i][0]
    print(ans)

if __name__ == '__main__':
    main()