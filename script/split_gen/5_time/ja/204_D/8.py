def main():
    # input
    n = int(input())
    t = list(map(int, input().split()))
    # compute
    if n == 1:
        ans = t[0]
    elif n == 2:
        if t[0] < t[1]:
            ans = t[1]
        else:
            ans = t[0]
    else:
        t.sort()
        ans = t[-1]
        for i in range(n-2):
            ans += t[i]
    # output
    print(ans)
