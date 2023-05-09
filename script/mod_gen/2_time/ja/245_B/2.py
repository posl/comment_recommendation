def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
    else:
        for i in range(N-1):
            if A[i+1] - A[i] >= 2:
                print(A[i] + 1)
                break
        else:
            print(A[-1] + 1)
main()

if __name__ == '__main__':
    main()