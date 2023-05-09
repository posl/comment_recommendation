def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K+A[0])
    d = []
    for i in range(N):
        d.append(A[i+1]-A[i])
    print(K-max(d))

if __name__ == '__main__':
    main()