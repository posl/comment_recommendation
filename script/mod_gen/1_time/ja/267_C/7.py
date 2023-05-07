def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-M+1):
        sum += sum(A[i:i+M])
    print(sum)
    return

if __name__ == '__main__':
    main()