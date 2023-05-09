def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    ans = []
    ans.append(1)
    for i in range(N-1):
        ans.append(AB[i][0])
        ans.append(AB[i][1])
    ans.append(1)
    print(*ans)

if __name__ == '__main__':
    main()