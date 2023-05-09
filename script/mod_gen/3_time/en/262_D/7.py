def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(1, 2**N):
        S = 0
        for j in range(N):
            if i >> j & 1:
                S += A[j]
        if S % bin(i).count('1') == 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()