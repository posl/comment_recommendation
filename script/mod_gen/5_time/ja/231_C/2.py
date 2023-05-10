def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        cnt = 0
        for a in A:
            if a >= x:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()