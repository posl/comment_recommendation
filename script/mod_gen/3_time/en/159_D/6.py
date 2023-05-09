def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N+1)
    for i in A:
        B[i] += 1
    for i in range(1, N+1):
        if B[i] > 1:
            print((B[i] * (B[i]-1))//2)
        else:
            print(0)

if __name__ == '__main__':
    main()