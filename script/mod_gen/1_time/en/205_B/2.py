def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] += 1
    if B.count(1) == N:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()