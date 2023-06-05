def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    for i in range(0, N):
        for j in range(i+1, N):
            if abs(A[i] - A[j]) > max:
                max = abs(A[i] - A[j])
    print(max)

if __name__ == '__main__':
    main()