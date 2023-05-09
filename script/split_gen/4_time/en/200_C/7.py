def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a = [x%200 for x in a]
    a.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] == a[j]:
                ans += 1
    print(ans)
