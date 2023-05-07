def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()
    max = -1
    for i in range(0,N-1):
        for j in range(i+1,N):
            if (A[i] + A[j]) % 2 == 0:
                if max < A[i] + A[j]:
                    max = A[i] + A[j]
    print(max)

if __name__ == '__main__':
    main()