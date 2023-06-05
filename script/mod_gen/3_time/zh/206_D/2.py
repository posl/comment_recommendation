def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    i = 0
    count = 0
    while i < N:
        if i == N-1:
            count += 1
            break
        if A[i] == A[i+1]:
            i += 2
            count += 1
        else:
            i += 1
    print(count)

if __name__ == '__main__':
    main()