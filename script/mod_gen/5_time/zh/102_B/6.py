def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_num = 0
    for i in range(N):
        for j in range(i+1, N):
            if max_num < abs(A[i] - A[j]):
                max_num = abs(A[i] - A[j])
    print(max_num)

if __name__ == '__main__':
    main()