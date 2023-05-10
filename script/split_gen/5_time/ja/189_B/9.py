def main():
    n, x = map(int, input().split())
    v_p = [list(map(int, input().split())) for _ in range(n)]
    alc = 0
    for i in range(n):
        alc += v_p[i][0] * v_p[i][1] / 100
        if alc > x:
            print(i + 1)
            exit()
    print(-1)
