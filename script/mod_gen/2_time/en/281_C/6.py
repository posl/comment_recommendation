def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T)
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
        #print("sum", sum)
        if T <= sum:
            print(i+1, T-(sum-A[i]))
            break

if __name__ == '__main__':
    main()