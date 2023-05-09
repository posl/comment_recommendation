def main():
    N, A, B = map(int, input().split())
    S = input()
    S = S[::-1]
    cnt = 0
    for i in range(N//2):
        if S[i] == S[N-1-i]:
            continue
        elif S[i] == "a":
            cnt += A
        elif S[i] == "b":
            cnt += B
        elif S[N-1-i] == "a":
            cnt += A
        elif S[N-1-i] == "b":
            cnt += B
        else:
            print(-1)
            return
    if N%2 == 1:
        if S[N//2] == "a":
            cnt += A
        elif S[N//2] == "b":
            cnt += B
    print(cnt)
