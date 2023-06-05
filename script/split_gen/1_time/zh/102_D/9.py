def main():
    n = int(input())
    a = list(map(int, input().split()))
    maxs = [a[0]]
    mins = [a[0]]
    for i in range(1, n):
        maxs.append(max(maxs[i-1], a[i]))
        mins.append(min(mins[i-1], a[i]))
    ans = 0
    for i in range(n-1):
        ans = max(ans, abs(maxs[i]-mins[i+1]))
    print(ans)
