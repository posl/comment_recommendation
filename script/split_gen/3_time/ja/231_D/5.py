def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 'Yes'
    for i in range(M):
        if AB[i][0] == AB[i][1] - 1:
            ans = 'No'
    print(ans)
