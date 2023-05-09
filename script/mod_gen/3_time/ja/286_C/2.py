def main():
    N, A, B = map(int, input().split())
    S = input()
    if S == S[::-1]:
        print(0)
        return
    if A > B:
        print(0)
        return
    if S[0] != S[-1]:
        print(A)
        return
    cnt = 1
    for i in range(N):
        if S[i] != S[-i-1]:
            break
        cnt += 1
    if cnt == N:
        print((N-1)*B)
        return
    if cnt == N-1:
        print(A)
        return
    if S[0] == S[-1]:
        print((cnt//2)*B + A)
        return

if __name__ == '__main__':
    main()