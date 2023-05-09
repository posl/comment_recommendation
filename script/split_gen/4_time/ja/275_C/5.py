def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    #s = input()
    #h,w = map(int, input().split())
    #a = [list(map(int, input().split())) for _ in range(h)]
    #s = [input() for _ in range(3)]
    s = [input() for _ in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                ans += 1
    print(ans)
    return
