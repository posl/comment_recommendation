def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    #print(N, A, X)
    B = A*(10**100)
    #print(B)
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i+1)
            break

if __name__ == '__main__':
    main()