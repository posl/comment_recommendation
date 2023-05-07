def main():
    n = int(input())
    A = []
    B = []
    for _ in range(n):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(n):
        ans += A[i]/B[i]
    ans /= 2
    for i in range(n):
        ans -= A[i]/B[i]
        if ans <= 0:
            ans += A[i]/B[i]
            break
    ans *= B[i]
    print(ans)
