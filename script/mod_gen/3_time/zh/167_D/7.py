def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0,0)
    now = 1
    for i in range(K):
        now = A[now]
    print(now)

if __name__ == '__main__':
    main()