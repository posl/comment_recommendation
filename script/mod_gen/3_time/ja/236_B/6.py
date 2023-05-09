def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if A[i*4] != A[i*4+1] or A[i*4+1] != A[i*4+2] or A[i*4+2] != A[i*4+3]:
            print(A[i*4])
            break

if __name__ == '__main__':
    main()