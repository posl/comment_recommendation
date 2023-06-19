def get_second_min(p, i):
    if p[i-1] < p[i]:
        if p[i] < p[i+1]:
            return p[i]
        else:
            if p[i-1] < p[i+1]:
                return p[i+1]
            else:
                return p[i-1]
    else:
        if p[i] > p[i+1]:
            return p[i]
        else:
            if p[i-1] < p[i+1]:
                return p[i-1]
            else:
                return p[i+1]
n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(1, n-1):
    if get_second_min(p, i) == p[i]:
        count += 1
print(count)
