def main():
    n = int(input())
    ladders = [list(map(int, input().split())) for _ in range(n)]
    ladders.sort(key=lambda x: x[1])
    ans = 1
    for a, b in ladders:
        if ans < a:
            ans = b
    print(ans)
