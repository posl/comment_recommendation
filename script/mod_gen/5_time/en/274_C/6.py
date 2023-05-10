def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    result = [0] * (2**N)
    #print(result)
    for i in range(N):
        #print(i)
        result[A[i]-1] = i+1
    #print(result)
    for i in range(2**N):
        #print(i)
        if result[i] == 0:
            result[i] = result[i-1]
    #print(result)
    for i in range(2**N):
        print(result[i]-1)

if __name__ == '__main__':
    main()