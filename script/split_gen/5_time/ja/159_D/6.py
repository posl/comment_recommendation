def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    a.append(-1)
    ans = [0 for _ in range(n)]
    count = 1
    for i in range(n):
        if a[i] == a[i+1]:
            count += 1
        else:
            ans[a[i]-1] = count
            count = 1
    for i in range(n):
        print(n-ans[i])
