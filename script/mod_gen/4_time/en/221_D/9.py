def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[0] = AB[0][1]
        else:
            ans[i] = ans[i-1] + AB[i][1]
    for i in range(N):
        if i == 0:
            print(ans[N-1])
        else:
            print(ans[N-1] - ans[i-1])

if __name__ == '__main__':
    main()