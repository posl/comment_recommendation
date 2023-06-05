def main():
    n = int(input())
    ab = []
    for i in range(n-1):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[1])
    ab.sort(key=lambda x: x[0])
    print(ab)
    ans = [1]
    for i in range(n-1):
        if ab[i][0] == ans[-1]:
            ans.append(ab[i][1])
        elif ab[i][1] == ans[-1]:
            ans.append(ab[i][0])
    ans.append(1)
    print(*ans)

if __name__ == '__main__':
    main()