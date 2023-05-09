def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        odd = 0
        for j in range(N):
            if A[j] % 2 == 1:
                odd += 1
        print(odd)

if __name__ == '__main__':
    main()