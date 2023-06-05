def solve(n, ti):
    if n == 1:
        return ti[0]
    elif n == 2:
        return max(ti[0], ti[1])
    elif n == 3:
        return max(ti[0]+ti[1], ti[2])
    elif n == 4:
        return max(ti[0]+ti[1], ti[2]+ti[3])
    elif n == 5:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3])
    elif n == 6:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3], ti[0]+ti[5]+ti[3])
    elif n == 7:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3], ti[0]+ti[5]+ti[3], ti[0]+ti[2]+ti[6])
    elif n == 8:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3], ti[0]+ti[5]+ti[3], ti[0]+ti[2]+ti[6], ti[0]+ti[5]+ti[7])
    elif n == 9:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3], ti[0]+ti[5]+ti[3], ti[0]+ti[2]+ti[6], ti[0]+ti[5]+ti[7], ti[0]+ti[8]+ti[1])
    elif n == 10:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3], ti[0]+ti[5]+ti[3], ti[0]+ti[2]+ti[6], ti[0]+ti[5]+ti[7], ti[0]+ti[8]+ti[1], ti[0]+ti[8]+ti[9])
    else:
        return 0
n = int(input())
ti = list(map(int, input().split()))
ti.sort(reverse=True)
print(solve(n
