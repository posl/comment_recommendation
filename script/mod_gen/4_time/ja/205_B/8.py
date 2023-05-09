def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    # compute
    A.sort()
    for i in range(N):
        if A[i] != i+1:
            print("No")
            exit()
    # output
    print("Yes")

if __name__ == '__main__':
    main()