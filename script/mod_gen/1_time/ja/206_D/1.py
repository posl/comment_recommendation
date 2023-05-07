def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N//2):
        if A[i] != A[N-1-i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()