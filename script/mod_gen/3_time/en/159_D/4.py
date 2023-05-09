def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for a in A:
        B[a-1] += 1
    for i in range(N):
        if B[i] == 0:
            print(0)
        else:
            print((B[i]-1)*B[i]//2)

if __name__ == '__main__':
    main()