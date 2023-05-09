def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        count = 0
        for j in range(N):
            if A[j] % 2 != 0:
                count += 1
        print(count)

if __name__ == '__main__':
    main()