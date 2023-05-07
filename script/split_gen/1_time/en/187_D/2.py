def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    ans = 0
    takahashi = 0
    aoki = 0
    for i in range(N):
        aoki += AB[i][0]
    for i in range(N):
        takahashi += AB[i][1]
        aoki -= AB[i][0]
        ans += 1
        if takahashi > aoki:
            break
    print(ans)
