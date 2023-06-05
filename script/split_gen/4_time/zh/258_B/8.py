def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = -1
    for i in range(n):
        for j in range(n):
            for k in range(8):
                d = 10 ** 9
                ni = i
                nj = j
                for l in range(n):
                    ni += di[k]
                    nj += dj[k]
                    if ni == -1:
                        ni = n - 1
                    elif ni == n:
                        ni = 0
                    if nj == -1:
                        nj = n - 1
                    elif nj == n:
                        nj = 0
                    d *= 10
                    d += a[ni][nj]
                ans = max(ans, d)
    print(ans)
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
