def main():
    N, M = map(int, input().split())
    f = [0] * (N + 2)
    for i in range(M):
        a, b = map(int, input().split())
        f[a] += 1
        f[b + 1] -= 1
    for i in range(1, N + 1):
        f[i] += f[i - 1]
    for i in range(1, N + 1):
        if f[i] == 0:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()