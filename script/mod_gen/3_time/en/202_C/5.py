def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()
    count = 0
    for i in range(N):
        count += len([j for j in range(N) if A[i] == B[C[j] - 1]])
    print(count)

if __name__ == '__main__':
    main()