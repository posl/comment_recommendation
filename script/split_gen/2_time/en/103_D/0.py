def main():
    N, M = map(int, input().split())
    A, B = [], []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    ans = 0
    for i in range(M):
        a = A[i]
        b = B[i]
        for j in range(i+1, M):
            c = A[j]
            d = B[j]
            if (a < c < b < d) or (c < a < d < b):
                ans += 1
                break
    print(ans)
