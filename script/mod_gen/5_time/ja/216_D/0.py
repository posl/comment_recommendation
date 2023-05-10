def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        A.append(list(map(int, input().split()))[1:])
    color = [0] * (N+1)
    for i in range(M):
        for j in range(len(A[i])):
            color[A[i][j]] += 1
    for i in range(len(color)):
        if color[i] % 2 == 1:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    main()