def on_off_combination(n,m,k,s,p):
    # n: number of switches
    # m: number of bulbs
    # k: number of switches connected to bulb
    # s: switches connected to bulb
    # p: state of bulb
    # return: number of combinations to turn on all bulbs
    comb = []
    for i in range(2**n):
        switch = []
        for j in range(n):
            if (i>>j)&1:
                switch.append(1)
            else:
                switch.append(0)
        comb.append(switch)
    count = 0
    for c in comb:
        bulb = []
        for i in range(m):
            light = 0
            for j in range(k[i]):
                light += c[s[i][j]-1]
            bulb.append(light%2)
        if bulb == p:
            count += 1
    return count

if __name__ == '__main__':
    on_off_combination()