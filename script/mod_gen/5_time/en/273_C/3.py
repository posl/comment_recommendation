def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    result = [0] * N
    for i in range(N):
        if i == 0:
            count += 1
        elif A[i] != A[i-1]:
            count += 1
        result[i] = count
    for i in range(N):
        print(result[A[i]-1])

if __name__ == '__main__':
    main()