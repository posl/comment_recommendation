def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(10**10)
    k = 0
    ans = [0]*n
    for i in range(n):
        if a[i] != a[i+1]:
            ans[k] += 1
            k = 0
        else:
            k += 1
    for i in range(n):
        print(ans[i])
