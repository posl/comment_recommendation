def main():
    n, x = map(int, input().split())
    v_p = [list(map(int, input().split())) for i in range(n)]
    alcohol = 0
    for i in range(n):
        alcohol += v_p[i][0] * v_p[i][1] / 100
        if alcohol > x:
            print(i+1)
            exit()
    print(-1)
