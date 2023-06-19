def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(M)]
    A.sort(key=lambda x: x[1])
    ans = 0
    bridge = 0
    for i in range(M):
        if A[i][0] > bridge:
            bridge = A[i][1] - 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()