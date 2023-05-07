def main():
    #N = int(input())
    #A = list(map(int, input().split()))
    N = 5
    A = [1, 1, 1, 1, 1]
    A.sort()
    print(A)
    print(A[N-1]-A[0])
    return

if __name__ == '__main__':
    main()