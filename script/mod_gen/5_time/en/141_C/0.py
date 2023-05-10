def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [0] * N
    for a in A:
        score[a-1] += 1
    for i in range(N):
        if K + score[i] - Q > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()