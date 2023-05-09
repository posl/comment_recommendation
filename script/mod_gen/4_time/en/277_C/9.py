def solve(n, ladders):
    #print(n, ladders)
    ladders.sort(key=lambda x:x[0])
    #print(ladders)
    min_floor = 1
    max_floor = 10**9
    for ladder in ladders:
        a = ladder[0]
        b = ladder[1]
        if a > min_floor:
            min_floor = a
        if b < max_floor:
            max_floor = b
        if min_floor > max_floor:
            return 0
    return max_floor - min_floor + 1

if __name__ == '__main__':
    solve()