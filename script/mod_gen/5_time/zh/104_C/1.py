def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for bits in range(1<<D):
        score = 0
        cnt = 0
        rest_max = -1
        for i in range(D):
            if bits & (1<<i):
                score += 100*(i+1)*pc[i][0] + pc[i][1]
                cnt += pc[i][0]
            else:
                rest_max = i
        if score < G:
            s1 = 100*(rest_max+1)
            need = (G-score+s1-1)//s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()