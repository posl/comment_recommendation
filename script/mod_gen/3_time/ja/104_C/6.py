def main():
    d, g = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(d)]
    ans = float("inf")
    for i in range(2**d):
        count = 0
        total = 0
        rest_max = -1
        for j in range(d):
            if ((i>>j) & 1):
                count += p[j][0]
                total += 100*(j+1)*p[j][0] + p[j][1]
            else:
                rest_max = j
        if total < g:
            s1 = 100*(rest_max+1)
            need = (g-total+s1-1)//s1
            if need >= p[rest_max][0]:
                continue
            count += need
        ans = min(ans, count)
    print(ans)

if __name__ == '__main__':
    main()