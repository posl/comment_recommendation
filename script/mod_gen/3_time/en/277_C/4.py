def main():
    n = int(input())
    ladders = [list(map(int, input().split())) for _ in range(n)]
    ladders.sort(key=lambda x: x[1])
    ans = 1
    for ladder in ladders:
        if ans < ladder[0]:
            ans = ladder[1]
    print(ans)

if __name__ == '__main__':
    main()