def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [[A[i],i+1] for i in range(len(A))]
    A.sort()
    A = [A[i][1] for i in range(len(A))]
    print(A[-2])

if __name__ == '__main__':
    main()