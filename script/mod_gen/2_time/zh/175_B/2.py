def triangle():
    n = int(input())
    sticks = list(map(int, input().split()))
    sticks.sort()
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if sticks[i] != sticks[j] and sticks[j] != sticks[k] and sticks[k] != sticks[i]:
                    if sticks[i] + sticks[j] > sticks[k]:
                        res += 1
    print(res)

if __name__ == '__main__':
    triangle()