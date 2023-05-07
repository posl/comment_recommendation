def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    p = [0] + p
    ans = 0
    for i in range(n, 0, -1):
        if ans < p[i]:
            ans = p[i]
    print(ans)
