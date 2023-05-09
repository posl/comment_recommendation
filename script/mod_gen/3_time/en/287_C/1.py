def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    u.sort()
    v.sort()
    if u[0] == 1 and v[-1] == N:
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()