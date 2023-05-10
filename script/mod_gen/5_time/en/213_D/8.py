def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    ans = [1]
    for i in range(N-1):
        if ans[-1] == AB[i][0]:
            ans.append(AB[i][1])
        elif ans[-1] == AB[i][1]:
            ans.append(AB[i][0])
        else:
            pass
    print(*ans)

if __name__ == '__main__':
    main()