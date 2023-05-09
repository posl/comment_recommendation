def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = [A[i + 1] - A[i] for i in range(N - 1)]
    B.append(K - A[-1] + A[0])
    print(K - max(B))

if __name__ == '__main__':
    main()