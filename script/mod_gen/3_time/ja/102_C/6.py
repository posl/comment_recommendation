def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A = sorted(A)
    if N % 2 == 0:
        b = A[N // 2 - 1]
        b2 = A[N // 2]
        print(min(sum([abs(x - (b + i)) for i, x in enumerate(A)]), sum([abs(x - (b2 + i)) for i, x in enumerate(A)])))
    else:
        b = A[N // 2]
        print(sum([abs(x - (b + i)) for i, x in enumerate(A)]))

if __name__ == '__main__':
    main()