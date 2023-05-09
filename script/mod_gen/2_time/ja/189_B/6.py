def main():
    N, X = map(int, input().split())
    A = 0
    for i in range(N):
        V, P = map(int, input().split())
        A += V * P
        if A > X * 100:
            print(i + 1)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()