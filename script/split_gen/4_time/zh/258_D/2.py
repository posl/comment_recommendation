def main():
    N, X = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for i in range(N):
        ans += AB[i][0] + AB[i][1]
        if ans > X:
            print(i)
            return
    print(N)
