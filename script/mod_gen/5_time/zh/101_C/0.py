def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    min = A[0]
    count = 0
    for i in range(n-k+1):
        min = A[i]
        for j in range(k):
            if A[i+j] < min:
                min = A[i+j]
        for j in range(k):
            A[i+j] = min
        count += 1
    print(count)

if __name__ == '__main__':
    main()