def main():
    N, A, B = map(int, input().split())
    S = input()
    count = 0
    for i in range(N):
        if S[i] != S[N - 1 - i]:
            if S[i] == 'a':
                count += A
            else:
                count += B
    if count == 0:
        print(0)
    elif count == A:
        print(A)
    elif count == B:
        print(B)
    else:
        print(2 * min(A, B))
