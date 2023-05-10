def main():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    #print(txa)
    ans = 0
    for i in range(n):
        t, x, a = txa[i][0], txa[i][1], txa[i][2]
        if i == 0:
            ans = a
        else:
            ans = max(ans + a, a)
        if i != n - 1:
            t_next, x_next = txa[i+1][0], txa[i+1][1]
            if t_next - t >= abs(x_next - x):
                ans = max(ans, a)
    print(ans)
