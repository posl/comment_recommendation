def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    ans = 1
    for i in range(n):
        if ans < ab[i][0]:
            ans = ab[i][0]
    print(ans)
