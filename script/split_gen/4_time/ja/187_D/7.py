def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0]+x[1], reverse=True)
    a_sum = sum([x[0] for x in ab])
    b_sum = 0
    ans = 0
    for x in ab:
        a_sum -= x[0]
        b_sum += x[0]+x[1]
        ans += 1
        if a_sum < b_sum:
            break
    print(ans)
