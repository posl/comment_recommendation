def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    dis = [A[i + 1] - A[i] for i in range(N)]
    print(K - max(dis))

if __name__ == '__main__':
    main()