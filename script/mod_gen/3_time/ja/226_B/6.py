def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #print(A)
    A.sort()
    #print(A)
    count = 1
    for i in range(1, N):
        if A[i] != A[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()