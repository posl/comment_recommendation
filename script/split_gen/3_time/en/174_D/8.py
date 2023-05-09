def main():
    N = int(input())
    c = list(input())
    R_count = c.count('R')
    W_count = N - R_count
    ans = 0
    for i in range(R_count):
        if c[i] == 'W':
            ans += 1
    print(ans)
