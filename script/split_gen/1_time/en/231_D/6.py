def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = "Yes"
    for i in range(M):
        if i == 0:
            a = AB[i][0]
            b = AB[i][1]
        else:
            if a == AB[i][0]:
                a = AB[i][0]
                b = AB[i][1]
            elif a < AB[i][0] and AB[i][0] < b:
                ans = "No"
                break
            else:
                a = AB[i][0]
                b = AB[i][1]
    print(ans)
