def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    D = [A[i+1]-A[i] for i in range(N-1)]
    D.append(K - A[-1] + A[0])
    print(K - max(D))

if __name__ == '__main__':
    main()