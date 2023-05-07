def main():
    n = int(input())
    ans = -1
    for i in range(n):
        a, p, x = map(int, input().split())
        if a < x:
            if ans == -1 or ans > p:
                ans = p
    print(ans)

if __name__ == '__main__':
    main()