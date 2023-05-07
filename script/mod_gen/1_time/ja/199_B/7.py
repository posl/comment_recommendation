def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(B)
    count = 0
    for i in range(1, 1001):
        for j in range(N):
            if i < A[j] or i > B[j]:
                break
            elif j == N-1:
                count += 1
    print(count)

if __name__ == '__main__':
    main()