def main():
    N, A, B = map(int, input().split())
    S = input()
    if S == S[::-1]:
        print(0)
        return
    cnt = 0
    for i in range(N):
        if S[i] != S[-i-1]:
            cnt += 1
    cnt //= 2
    if cnt == 1:
        print(min(A, B))
        return
    if cnt == 0:
        print(min(A, B*(N//2)))
        return
    print(min(A*(cnt-1)+B, A*cnt+B))
