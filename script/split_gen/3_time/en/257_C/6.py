def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    ans = 0
    for i in range(1,n):
        if s[i-1] == "0" and s[i] == "1":
            ans += 1
    if ans == 0:
        print(0)
        exit()
    ans += 2
    ans -= 1 if s[0] == "0" else 0
    ans -= 1 if s[-1] == "0" else 0
    for i in range(n):
        if s[i] == "0":
            if i == 0:
                ans += 1 if w[i] < w[i+1] else 0
            elif i == n-1:
                ans += 1 if w[i-1] < w[i] else 0
            else:
                ans += 1 if w[i-1] < w[i] and w[i] > w[i+1] else 0
    print(ans)
