def main():
    N, A, B = map(int, input().split())
    S = input()
    if A > B:
        print(N * B)
        return
    if len(set(S)) == 1:
        print(N * A // 2)
        return
    cnt = 0
    for i in range(N):
        if S[i] != S[N - i - 1]:
            cnt += 1
    if cnt == 1:
        print(N * A - A // 2)
        return
    print(N * A)
