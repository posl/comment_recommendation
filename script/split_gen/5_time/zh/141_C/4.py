def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [0] * N
    for i in A:
        score[i-1] += 1
    for i in score:
        if K + i - Q > 0:
            print("Yes")
        else:
            print("No")
