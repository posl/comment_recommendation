def main():
    n, m = map(int, input().split())
    cakes = []
    for i in range(n):
        x, y, z = map(int, input().split())
        cakes.append([x, y, z])
    #print(cakes)
    ans = 0
    for i in range(2**3):
        plus_minus = []
        for j in range(3):
            if ((i >> j) & 1):
                plus_minus.append(-1)
            else:
                plus_minus.append(1)
        #print(plus_minus)
        sum_list = []
        for j in range(n):
            sum_list.append(cakes[j][0]*plus_minus[0] + cakes[j][1]*plus_minus[1] + cakes[j][2]*plus_minus[2])
        #print(sum_list)
        sum_list.sort(reverse=True)
        #print(sum_list)
        tmp = 0
        for j in range(m):
            tmp += sum_list[j]
        #print(tmp)
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()