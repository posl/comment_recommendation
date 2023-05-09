def main():
    N, M = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(M)]
    A.sort(key=lambda x: x[1])
    ans = 0
    tmp = 0
    for a, b in A:
        if tmp < a:
            ans += 1
            tmp = b - 1
    print(ans)

if __name__ == '__main__':
    main()