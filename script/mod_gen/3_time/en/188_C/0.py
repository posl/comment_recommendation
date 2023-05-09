def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(a, i + 1) for i, a in enumerate(A)]
    A.sort()
    for i in range(N):
        A = [(max(a, b), i + 1) for i, (a, b) in enumerate(zip(A[::2], A[1::2]))]
    print(A[0][1])

if __name__ == '__main__':
    main()