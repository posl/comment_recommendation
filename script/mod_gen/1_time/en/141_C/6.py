def main():
    N, K, Q = map(int, input().split())
    A = []
    for i in range(Q):
        A.append(int(input()))
    score = [K] * N
    for i in range(Q):
        score[A[i]-1] += 1
    for i in range(N):
        if score[i] > Q:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()