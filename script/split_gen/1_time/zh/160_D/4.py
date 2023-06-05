def main():
    n, x, y = map(int, input().split())
    for k in range(1, n):
        ans = 0
        for i in range(1, n):
            for j in range(i+1, n+1):
                if i <= x and j >= y:
                    d = min(j-i, abs(i-x)+1+abs(j-y))
                elif i <= x:
                    d = min(j-i, abs(i-x)+1+abs(j-y))
                elif j >= y:
                    d = min(j-i, abs(i-x)+1+abs(j-y))
                else:
                    d = j-i
                if d == k:
                    ans += 1
        print(ans)
