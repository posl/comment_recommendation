def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if ans < ab[i][1]:
            ans = ab[i][1]
    print(ans)

if __name__ == '__main__':
    main()