def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    i = 1
    while i < N:
        if A[i] % A[0] == 0:
            A.pop(i)
            N -= 1
        else:
            i += 1
    print(N)

if __name__ == '__main__':
    main()