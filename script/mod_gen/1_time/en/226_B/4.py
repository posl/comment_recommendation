def main():
    N = int(input())
    D = set()
    for i in range(N):
        L, *A = map(int, input().split())
        D.add((L, tuple(A)))
    print(len(D))

if __name__ == '__main__':
    main()