def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    if A[i] + A[j] > A[k] and A[i] + A[k] > A[j] and A[j] + A[k] > A[i]:
                        count += 1
    print(count)

if __name__ == '__main__':
    main()