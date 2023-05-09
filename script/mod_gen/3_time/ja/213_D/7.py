def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    ans = [1]
    for i in range(2,N+1):
        for j in range(N-1):
            if i == AB[j][0]:
                ans.append(AB[j][1])
            elif i == AB[j][1]:
                ans.append(AB[j][0])
    ans.append(1)
    print(*ans)

if __name__ == '__main__':
    main()