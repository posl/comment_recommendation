def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N):
        B[i] = (A[i-1] - A[i])//2
    print(*B)
    return

if __name__ == '__main__':
    main()