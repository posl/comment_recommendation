def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    ans = 1
    tmp = X
    while True:
        if tmp == A[tmp]:
            break
        tmp = A[tmp]
        ans += 1
    print(ans)
