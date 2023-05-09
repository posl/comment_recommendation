def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    X = int(input())
    B = A * (10**100//N) + A[:(10**100%N)]
    #print(B)
    sumB = 0
    for i in range(len(B)):
        sumB += B[i]
        if sumB > X:
            print(i+1)
            break

if __name__ == '__main__':
    main()