def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    #print(N, S, Q, T, A, B)
    ans = S
    for i in range(Q):
        if T[i] == 1:
            ans = ans[:A[i]-1] + ans[B[i]-1] + ans[A[i]:B[i]-1] + ans[A[i]-1] + ans[B[i]:]
        else:
            ans = ans[N:] + ans[:N]
    print(ans)
