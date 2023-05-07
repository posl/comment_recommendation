def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    ans = 200000
    for i in range(1, N):
        ans = min(ans, c[:i].count('R') + c[i:].count('W'))
    print(ans)
