def main():
    N,M = map(int,input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    AB.sort()
    ans = 0
    for i in range(N):
        if M == 0:
            break
        if M <= AB[i][1]:
            ans += M*AB[i][0]
            M = 0
        else:
            ans += AB[i][0]*AB[i][1]
            M -= AB[i][1]
    print(ans)
