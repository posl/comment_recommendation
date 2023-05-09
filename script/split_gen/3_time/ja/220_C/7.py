def main():
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())
    s = sum(A)
    if s <= X:
        print(N*X//s)
    else:
        ans = 0
        for i in range(N):
            ans += 1
            X -= A[i]
            if X <= 0:
                break
        print(ans)
