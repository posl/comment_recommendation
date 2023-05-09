def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    AB = []
    for i in range(N):
        AB.append([A[i], B[i]])
    #print(AB)
    AB.sort()
    #print(AB)
    ans = 0
    for i in range(N):
        if M <= AB[i][1]:
            ans += AB[i][0] * M
            break
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]
    print(ans)
