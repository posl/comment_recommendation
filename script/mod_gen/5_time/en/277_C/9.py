def main():
    # input
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # compute
    AB.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        if AB[i][0] < ans:
            continue
        else:
            ans = AB[i][1]
    # output
    print(ans)

if __name__ == '__main__':
    main()