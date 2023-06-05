def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum < b_sum:
        print(0)
        return
    diff = []
    for i in range(n):
        diff.append(a[i] - b[i])
    diff.sort()
    diff.reverse()
    ans = 0
    for i in range(n):
        if a_sum >= b_sum:
            break
        a_sum -= diff[i]
        ans += 1
    print(ans)
