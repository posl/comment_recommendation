def solve(n,x,ab):
    a = [ab[i][0] for i in range(n)]
    b = [ab[i][1] for i in range(n)]
    #print(a)
    #print(b)
    min_time = min(a)
    #print(min_time)
    min_index = a.index(min_time)
    #print(min_index)
    if x == 1:
        return min_time + b[min_index]
    else:
        if x % 2 == 0:
            return min_time * x + b[min_index]
        else:
            return min_time * x + min_time + b[min_index]
n,x = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
print(solve(n,x,ab))
