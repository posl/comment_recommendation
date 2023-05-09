def main():
    n = int(input())
    x = [int(i) for i in input().split()]
    ans = 1000000000000
    for p in range(1,101):
        tmp = 0
        for i in range(n):
            tmp += (x[i] - p) ** 2
        ans = min(ans,tmp)
    print(ans)
