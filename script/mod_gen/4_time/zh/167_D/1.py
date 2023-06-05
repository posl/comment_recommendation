def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [False for _ in range(N)]
    cnt = 0
    while not visited[0]:
        visited[cnt] = True
        cnt = A[cnt] - 1
    cnt2 = 0
    while visited[cnt]:
        visited[cnt] = False
        cnt = A[cnt] - 1
        cnt2 += 1
    K %= cnt2
    for _ in range(K):
        cnt = A[cnt] - 1
    print(cnt+1)

if __name__ == '__main__':
    main()