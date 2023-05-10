def main():
    N, K = map(int, input().split())
    A = [0]*N
    for i in range(K):
        d = int(input())
        A[i] = list(map(int, input().split()))
    print(N - len(set(sum(A, []))))

if __name__ == '__main__':
    main()