def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    AB = list(zip(A, B))
    AB.sort()
    ans = 0
    for i in range(N):
        if M <= 0:
            break
        if M <= AB[i][1]:
            ans += AB[i][0] * M
            M = 0
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]
    print(ans)
