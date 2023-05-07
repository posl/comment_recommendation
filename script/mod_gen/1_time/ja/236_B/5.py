def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    count = [0] * N
    for i in range(4 * N - 1):
        count[A[i] - 1] += 1
    
    for i in range(N):
        if count[i] % 2 == 1:
            print(i + 1)
            break

if __name__ == '__main__':
    main()