def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 1
    pos = 0
    for i in range(N):
        pos += L[i]
        if pos <= X:
            ans += 1
        else:
            break
    print(ans)
