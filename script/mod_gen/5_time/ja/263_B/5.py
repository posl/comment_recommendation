def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == 1:
            ans = i + 1
            break
    print(ans)

if __name__ == '__main__':
    main()