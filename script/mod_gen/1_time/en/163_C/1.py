def main():
    N = int(input())
    A = list(map(int, input().split()))
    subordinates = [0] * N
    for i in range(N-1):
        subordinates[A[i]-1] += 1
    for i in range(N):
        print(subordinates[i])

if __name__ == '__main__':
    main()