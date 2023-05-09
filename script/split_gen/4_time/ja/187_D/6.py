def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab = sorted(ab, key=lambda x: x[0]+x[1], reverse=True)
    a = sum([x[0] for x in ab])
    b = sum([x[1] for x in ab])
    ans = 0
    while a >= b:
        ans += 1
        a -= ab[ans-1][0]
        b -= ab[ans-1][1]
    print(ans)
