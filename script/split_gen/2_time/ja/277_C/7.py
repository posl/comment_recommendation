def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    for a, b in AB:
        if ans < a:
            ans = a
        ans = b
    print(ans)
