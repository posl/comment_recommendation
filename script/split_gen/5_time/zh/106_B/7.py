def solve(n):
    cnt = 0
    for i in range(1,n+1,2):
        div = 0
        for j in range(1,i+1):
            if i%j == 0:
                div += 1
        if div == 8:
            cnt += 1
    return cnt
