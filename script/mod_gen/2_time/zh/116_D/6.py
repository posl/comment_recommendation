def main():
    N, K = [int(x) for x in input().split()]
    sushis = []
    for i in range(N):
        t_i, d_i = [int(x) for x in input().split()]
        sushis.append((t_i, d_i))
    sushis.sort(key=lambda x: x[1], reverse=True)
    sushis.sort(key=lambda x: x[0])
    #print(sushis)
    used = []
    ans = 0
    count = 0
    for t_i, d_i in sushis:
        if t_i in used:
            ans += d_i
        else:
            if count < K:
                ans += d_i
                used.append(t_i)
                count += 1
    print(ans)

if __name__ == '__main__':
    main()