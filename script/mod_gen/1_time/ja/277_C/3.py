def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for a, b in AB:
        ans = max(ans, b)
    print(ans)

if __name__ == '__main__':
    main()