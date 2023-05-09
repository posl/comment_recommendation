def main():
    N, M = map(int, input().split())
    A = [0] * N
    for _ in range(M):
        *x, = map(int, input().split())
        for i in range(1, x[0]+1):
            A[x[i]-1] += 1
    if A.count(0) == 0:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()