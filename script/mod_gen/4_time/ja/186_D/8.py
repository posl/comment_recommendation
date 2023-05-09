def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    sum = 0
    for i in range(N-1):
        sum += (A[i+1]-A[i])*(i+1)*(N-i-1)
        #print(sum)
    print(sum)

if __name__ == '__main__':
    main()