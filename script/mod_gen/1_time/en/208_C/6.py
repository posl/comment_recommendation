def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if K > N:
            print(1)
        else:
            if i < K:
                print(1)
            else:
                print(0)

if __name__ == '__main__':
    main()