def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] - x[1], reverse=True)
    ans = 0
    for a, b in AB:
        if a >= b:
            ans += 1
        else:
            break
    print(ans)
