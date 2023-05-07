def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        x = int(input())
        cnt = 0
        for a in A:
            if a >= x:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()