def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    #print(N, K, Q, A)
    #print(N, K, Q, A)
    #print("A: ", A)
    score = [K] * N
    #print("score: ", score)
    for i in range(Q):
        score[A[i] - 1] += 1
        #print("score: ", score)
    for i in range(N):
        if score[i] - Q <= 0:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()