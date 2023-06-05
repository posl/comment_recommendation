def main():
    N, K, Q = map(int, input().split())
    score = [K] * N
    for _ in range(Q):
        ans = int(input())
        score[ans - 1] += 1
    for i in range(N):
        if score[i] - Q <= 0:
            print("No")
        else:
            print("Yes")
