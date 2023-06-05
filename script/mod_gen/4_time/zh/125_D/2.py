def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    if N == 2:
        print(A[1] - A[0])
        return
    if A[0] >= 0:
        print(sum(A) - 2 * A[0])
        return
    if A[-1] <= 0:
        print(-sum(A) + 2 * A[-1])
        return
    print(sum([abs(i) for i in A]))

if __name__ == '__main__':
    main()