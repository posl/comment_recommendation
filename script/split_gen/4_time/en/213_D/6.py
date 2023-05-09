def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort()
    ans = [1]
    for i in range(N-1):
        if AB[i][0] == ans[-1]:
            ans.append(AB[i][1])
        elif AB[i][1] == ans[-1]:
            ans.append(AB[i][0])
    print(*ans)
