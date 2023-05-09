def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 1
    for i in range(N):
        if ans < AB[i][0]:
            break
        ans = AB[i][1]
    print(ans)

if __name__ == '__main__':
    main()