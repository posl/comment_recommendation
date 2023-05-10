def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_height = 0
    total_height = 0
    for i in range(N):
        if A[i] >= max_height:
            total_height += A[i] - max_height
            max_height = A[i]
        else:
            max_height = A[i]
    print(total_height)

if __name__ == '__main__':
    main()