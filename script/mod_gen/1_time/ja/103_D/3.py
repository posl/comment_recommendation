def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    i = 0
    while i < M:
        ans += 1
        j = i
        while j < M and AB[i][1] >= AB[j][0]:
            j += 1
        i = j
    print(ans)

if __name__ == '__main__':
    main()