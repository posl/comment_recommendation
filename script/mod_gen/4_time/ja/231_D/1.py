def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print('Yes' if len(set(A + B)) == N else 'No')

if __name__ == '__main__':
    main()