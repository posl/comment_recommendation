def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] += 1
    for i in range(N):
        print(sum([1 for j in range(N) if B[j] > B[i]])+1)

if __name__ == '__main__':
    main()