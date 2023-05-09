def main():
    N, K = map(int, input().split())
    Snuke = [0] * N
    for i in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for j in range(d):
            Snuke[A[j] - 1] += 1
    print(Snuke.count(0))

if __name__ == '__main__':
    main()