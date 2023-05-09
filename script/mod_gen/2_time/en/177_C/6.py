def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i] * A[i+1]
    print(sum)
main()

if __name__ == '__main__':
    main()