def main():
    N, M = map(int, input().split())
    k = [0] * M
    a = [[] for _ in range(M)]
    for i in range(M):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    #print(N, M, k, a)
    #print(N, M, k, a)
    if M % 2 == 1:
        print('No')
        return
    #print(N, M, k, a)
    #print(N, M, k, a)
    for i in range(M):
        for j in range(k[i]):
            a[i][j] -= 1
    #print(N, M, k, a)
    #print(N, M, k, a)
    color = [0] * N
    for i in range(M):
        color[a[i][0]] += 1
    #print(N, M, k, a)
    #print(N, M, k, a)
    for i in range(N):
        if color[i] >= 3:
            print('No')
            return
    #print(N, M, k, a)
    #print(N, M, k, a)
    for i in range(N):
        if color[i] == 2:
            start = i
            break
    #print(N, M, k, a)
    #print(N, M, k, a)
    now = start
    next = a[now][1]
    #print(N, M, k, a)
    #print(N, M, k, a)
    for i in range(N):
        #print(now, next)
        if color[now] != 2:
            print('No')
            return
        if next == start:
            print('Yes')
            return
        now = next
        next = a[now][1]
    print('No')
    return

if __name__ == '__main__':
    main()