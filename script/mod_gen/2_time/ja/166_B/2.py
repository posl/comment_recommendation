def main():
    N, K = map(int, input().split())
    A = [0] * N
    for i in range(K):
        d = int(input())
        for j in map(int, input().split()):
            A[j - 1] += 1
    print(A.count(0))

if __name__ == '__main__':
    main()