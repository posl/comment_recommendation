def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    C = [A[i] + B[i] for i in range(N)]
    C.sort(reverse = True)
    ans = 0
    for i in range(N):
        if i%2 == 0:
            ans += C[i]
    print(ans)
