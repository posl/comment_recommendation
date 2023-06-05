def main():
    n, m = map(int, input().split())
    switch = []
    for i in range(m):
        switch.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**n):
        on = [0]*m
        for j in range(n):
            if (i>>j)&1:
                for k in range(m):
                    if j+1 in switch[k][1:]:
                        on[k] += 1
        if on == p:
            ans += 1
    print(ans)
