def main():
    N, M = map(int, input().split())
    A = [0] * N
    for i in range(M):
        input()
        for x in map(int, input().split()):
            A[x - 1] += 1
    print('Yes' if all(x % 2 == 0 for x in A) else 'No')

if __name__ == '__main__':
    main()