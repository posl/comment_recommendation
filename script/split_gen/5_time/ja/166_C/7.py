def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]
    answer = 0
    for i in range(n):
        check = True
        for j in range(m):
            if ab[j][0] == i+1:
                if h[i] <= h[ab[j][1]-1]:
                    check = False
                    break
        if check:
            answer += 1
    print(answer)
