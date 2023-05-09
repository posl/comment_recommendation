def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    total = 0
    for a in A:
        total += a
    if total > N:
        print(-1)
    else:
        print(N-total)

if __name__ == '__main__':
    main()