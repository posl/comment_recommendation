def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        count = 0
        for j in range(len(A)):
            if A[j] == x:
                count += 1
            if count == k:
                print(j + 1)
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()