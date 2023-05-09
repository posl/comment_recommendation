def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    i = X - 1
    ans = 0
    while True:
        ans += 1
        if A[i] == X:
            print(ans)
            break
        else:
            i = A[i] - 1
