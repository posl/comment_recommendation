def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))
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
