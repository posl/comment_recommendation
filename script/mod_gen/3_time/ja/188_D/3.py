def main():
    N, C = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(N)]
    abc.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        a, b, c = abc[i]
        ans += c
        for j in range(i + 1, N):
            if abc[j][0] <= b:
                abc[j][0] = b + 1
            else:
                break
    abc.sort(key=lambda x: x[0])
    for i in range(N):
        a, b, c = abc[i]
        ans += min(C, c) * (b - a + 1)
    print(ans)

if __name__ == '__main__':
    main()