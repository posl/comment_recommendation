def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(0, 4*N-1, 2):
        if A[i] != A[i+1]:
            print(A[i])
            break
    else:
        print(A[-1])

if __name__ == '__main__':
    main()