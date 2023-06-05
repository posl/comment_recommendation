def solve(n, lst):
    lst.sort(key=lambda x:x[0]+x[1])
    return lst[-1][0]+lst[-2][1]
n = int(input())
lst = []
for i in range(n):
    a,b = map(int, input().split())
    lst.append((a,b))
print(solve(n,lst))
