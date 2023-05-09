def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[0] % 2 == 0:
        print(A[0])
    else:
        for i in range(1, N):
            if A[i] % 2 == 0:
                print(A[i])
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()