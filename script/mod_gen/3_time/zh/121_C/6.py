def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a_b = list(zip(a,b))
    a_b.sort()
    sum_b = 0
    sum_money = 0
    for i in range(n):
        if sum_b + a_b[i][1] <= m:
            sum_b += a_b[i][1]
            sum_money += a_b[i][0] * a_b[i][1]
        else:
            sum_money += a_b[i][0] * (m - sum_b)
            break
    print(sum_money)

if __name__ == '__main__':
    main()