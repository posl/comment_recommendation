def main():
    n = int(input())
    ans = 0
    for i in range(n):
        a = int(input())
        for j in range(a):
            x, y = map(int, input().split())
            if y == 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()