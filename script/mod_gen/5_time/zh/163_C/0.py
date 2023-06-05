def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] * n
    for i in range(n-1):
        B[A[i]-1] += 1
    for i in range(n):
        print(B[i])

if __name__ == '__main__':
    main()