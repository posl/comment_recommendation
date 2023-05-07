def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(3 ** N):
        color = [0] * N
        for j in range(N):
            color[j] = i // (3 ** j) % 3
        ok = True
        for j in range(M):
            if color[A[j] - 1] == color[B[j] - 1]:
                ok = False
        if ok:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()