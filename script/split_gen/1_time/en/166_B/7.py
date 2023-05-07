def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(int(input()))
        A = list(map(int, input().split()))
        d.append(A)
    #print(d)
    ans = 0
    for i in range(1, N + 1):
        for j in range(0, len(d), 2):
            if i in d[j + 1]:
                break
        else:
            ans += 1
    print(ans)
