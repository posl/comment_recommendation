def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        if x not in A:
            print(-1)
        else:
            print(A.index(x, k-1)+1)

if __name__ == '__main__':
    main()