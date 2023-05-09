def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A = [x - (i + 1) for i, x in enumerate(A)]
    A.sort()
    if N % 2 == 1:
        b = A[N//2]
    else:
        b = (A[N//2-1] + A[N//2]) // 2
    print(sum([abs(x - b) for x in A]))

if __name__ == '__main__':
    main()