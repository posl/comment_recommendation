def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = 0
    for i in range(N):
        if X == 1:
            ans = i+1
            break
        else:
            X = A[X]
    print(ans)
