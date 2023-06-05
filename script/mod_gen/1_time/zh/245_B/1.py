def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    m = 0
    for i in range(0, N):
        if A[i] > m:
            print(m)
            exit()
        elif A[i] == m:
            m += 1
    print(m)

if __name__ == '__main__':
    main()