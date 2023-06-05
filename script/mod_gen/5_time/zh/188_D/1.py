def solve(n,c,events):
    events.sort()
    dp = [0]
    for day in range(1,events[-1][1]+1):
        dp.append(dp[-1]+c)
        for a,b,p in events:
            if b < day:
                continue
            if day < a:
                dp[-1] += p
            else:
                dp[-1] += min(p,(day-a+1)*c)
    return min(dp)
n,c = map(int,input().split())
events = []
for _ in range(n):
    a,b,p = map(int,input().split())
    events.append((a,b,p))
print(solve(n,c,events))
