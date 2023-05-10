def main():
    n = int(input())
    ab = [list(map(int, input().split())) for i in range(n)]
    ab.sort(key=lambda x: x[1])
    ans = 0
    for i in range(n):
        if ab[i][0] < ans:
            continue
        else:
            ans = ab[i][1]
    print(ans)

if __name__ == '__main__':
    main()