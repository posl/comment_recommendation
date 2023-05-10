def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(M)
    B = [0] * N
    for i in range(N):
        B[i] = A[i + 1] - A[i] - 1
    if M == 1:
        print(0)
    else:
        if B[0] == 0:
            B.remove(0)
        if len(B) == 0:
            print(0)
        else:
            m = min(B)
            ans = 0
            for i in range(len(B)):
                ans += -(-B[i] // m)
            print(ans)
