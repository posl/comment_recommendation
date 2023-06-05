def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    count = 0
    for i in range(0, N):
        for j in range(i+1, N):
            if A[i] != A[j]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()