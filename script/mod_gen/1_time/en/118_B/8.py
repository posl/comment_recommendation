def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(set(map(int, input().split()[1:])))
    print(sum(1 for i in range(1, M + 1) if all(i in a for a in A)))

if __name__ == '__main__':
    main()