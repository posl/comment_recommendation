def main():
    X = input()
    M = int(input())
    d = int(max(X))
    ans = 0
    for i in range(d+1,M+1):
        n = int(X, i)
        if ans < n <= M:
            ans = n
    print(ans)
