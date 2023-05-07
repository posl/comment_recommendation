def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = "No"
    for i in range(4):
        if i != 0:
            S = [[x[1], -x[0]] for x in S]
        for dx in range(-10, 11):
            for dy in range(-10, 11):
                if [[x[0]+dx, x[1]+dy] for x in S] == T:
                    ans = "Yes"
                    break
    print(ans)
