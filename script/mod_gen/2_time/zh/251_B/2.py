def main():
    N,W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
        if sum > W:
            print(i)
            return
    print(N)
    return

if __name__ == '__main__':
    main()