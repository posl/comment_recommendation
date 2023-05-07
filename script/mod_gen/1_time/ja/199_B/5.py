def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        count += B[i] - A[i] + 1
    print(count)

if __name__ == '__main__':
    main()