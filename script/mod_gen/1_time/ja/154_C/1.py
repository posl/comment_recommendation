def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print('NO')
            return
    print('YES')

if __name__ == '__main__':
    main()