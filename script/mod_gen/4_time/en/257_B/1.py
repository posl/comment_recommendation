def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    score = [0] * N
    for i in range(Q):
        score[L[i]-1] += 1
    for i in range(N):
        if K - Q + score[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()