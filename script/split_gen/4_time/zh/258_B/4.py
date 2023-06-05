def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(8):
                ni = i
                nj = j
                tmp = ''
                for l in range(n):
                    if not (0 <= ni < n and 0 <= nj < n):
                        break
                    tmp += a[ni][nj]
                    ni += di[k]
                    nj += dj[k]
                ans = max(ans, int(tmp))
    print(ans)
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
