def main():
    N, A, B = map(int, input().split())
    S = input()
    cnt = 0
    cnt_b = 0
    for i in range(N):
        if S[i] == S[N-i-1]:
            cnt += 1
        else:
            cnt_b += 1
    if cnt == N:
        print(0)
    elif cnt_b == 0:
        print(A*N)
    else:
        cnt_b = (cnt_b + 1) // 2
        print(A*N + B*cnt_b)
