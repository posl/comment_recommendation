def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i, N):
            if sum(A[i:j+1]) % (j-i+1) == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()