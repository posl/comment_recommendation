def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    ans = 0
    for i in range(N):
        ans += A[i]
        if ans > X:
            print(i+1)
            break
    else:
        print((X//ans)*N + N)
