def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 1
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[i] = 1
        else:
            if a[i] == a[i - 1]:
                ans[i] = count
            else:
                count += 1
                ans[i] = count
    for i in range(n):
        print(ans[i])
