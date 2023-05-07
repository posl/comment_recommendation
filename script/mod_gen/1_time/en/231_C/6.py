def main():
    N, Q = map(int, input().split())
    A = [int(i) for i in input().split()]
    A.sort()
    for i in range(Q):
        x = int(input())
        count = 0
        for j in range(N):
            if A[j] >= x:
                count += 1
        print(count)

if __name__ == '__main__':
    main()