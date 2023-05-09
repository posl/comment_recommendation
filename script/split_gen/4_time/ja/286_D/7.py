def main():
    N,X = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += A[i]*B[i]
    if ans <= X:
        print('Yes')
    else:
        print('No')
