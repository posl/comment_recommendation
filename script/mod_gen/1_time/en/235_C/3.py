def main():
    N, Q = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    for q in range(Q):
        x, k = [int(i) for i in input().split()]
        count = 0
        for i in range(N):
            if A[i] == x:
                count += 1
            if count == k:
                print(i + 1)
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()