def main():
    # input
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # compute
    score = [0] * N
    for i in range(Q):
        score[L[i] - 1] += 1
    for i in range(N):
        score[i] += K - Q
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()