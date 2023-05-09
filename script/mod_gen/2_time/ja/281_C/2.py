def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T)
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    if sum <= T:
        T = T % sum
    #print(T)
    for i in range(N):
        if T < A[i]:
            print(i+1, T)
            break
        else:
            T -= A[i]

if __name__ == '__main__':
    main()