def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(A[i], i+1) for i in range(len(A))]
    A = sorted(A, reverse=True)
    for i in range(len(A)):
        if i%2 == 1:
            print(A[i][1])
            break

if __name__ == '__main__':
    main()