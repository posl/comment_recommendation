def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    min_a = min(a)
    min_a_idx = a.index(min_a)
    min_x = min(x)
    min_x_idx = x.index(min_x)
    min_ans = min_a + min_x
    print(min_ans)
    for i in range(q):
        if i == min_x_idx:
            continue
        else:
            ans = 0
            for j in range(n):
                ans += abs(a[j] - x[i])
            print(ans)
    return
