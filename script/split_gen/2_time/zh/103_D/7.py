def main():
    N, M = map(int, input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i], b[i] = map(int, input().split())
    #print(a)
    #print(b)
    #print(N)
    #print(M)
    #print(N-1)
    ans = 0
    for i in range(M):
        if a[i] == 1 or b[i] == 1:
            ans += 1
    print(ans)
