def main():
    N, A, B = map(int, input().split())
    S = input()
    S = list(S)
    S2 = S[:]
    S2.reverse()
    if S == S2:
        print(0)
        return
    count = 0
    for i in range(N):
        if S[i] == S2[i]:
            count += 1
        else:
            break
    if count == N:
        print(0)
        return
    if count == N-2:
        print(min(A, B))
        return
    if count == N-1:
        print(B)
        return
    print(min(A, B)*count + B)
main()
