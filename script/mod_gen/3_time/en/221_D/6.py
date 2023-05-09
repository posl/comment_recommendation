def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #A[i] + B[i] - 1 = Day
    #A[i] + B[i] - 1 = A[i+1] + B[i+1] - 1
    #B[i] =

if __name__ == '__main__':
    main()