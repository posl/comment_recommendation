def main():
    n,m = [int(i) for i in input().split()]
    s = [input() for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            flag = True
            for k in range(m):
                if s[i][k] == 'x' and s[j][k] == 'x':
                    flag = False
                    break
            if flag:
                ans += 1
    print(ans)
