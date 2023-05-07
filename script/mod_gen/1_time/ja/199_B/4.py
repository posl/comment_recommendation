def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for x in range(1, 1001):
        if all(A[i] <= x <= B[i] for i in range(N)):
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()