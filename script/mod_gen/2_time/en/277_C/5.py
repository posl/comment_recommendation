def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for a, b in AB:
        if a <= ans:
            ans = b
        else:
            ans = a
    print(ans)

if __name__ == '__main__':
    main()