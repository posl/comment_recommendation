def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    max = 0
    for i in range(N):
        for j in range(i,N):
            for k in range(A[i],A[j]+1):
                sum = 0
                for l in range(i,j+1):
                    if A[l] >= k:
                        sum += k
                    else:
                        sum += A[l]
                if sum > max:
                    max = sum
    print(max)

if __name__ == '__main__':
    main()