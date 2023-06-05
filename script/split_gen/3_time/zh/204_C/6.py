def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                if A.count(i+1) > 0 and B.count(j+1) > 0:
                    if A.index(i+1) != B.index(j+1):
                        ans += 1
    print(ans)
