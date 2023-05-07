def main():
    N, M = map(int, input().split())
    l = [0] * (N+1)
    for _ in range(M):
        L, R = map(int, input().split())
        l[L-1] += 1
        l[R] -= 1
    print(sum([1 for i in range(N) if sum(l[:i+1]) == M]))

if __name__ == '__main__':
    main()