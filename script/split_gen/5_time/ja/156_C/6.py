def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10**10
    for i in range(1, 101):
        sum = 0
        for j in range(n):
            sum += (x[j]-i)**2
        ans = min(ans, sum)
    print(ans)
