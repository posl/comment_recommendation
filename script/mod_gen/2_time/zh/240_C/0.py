def jump(n,x,ab):
    if n == 0:
        return False
    if n == 1:
        if x == ab[0][0] or x == ab[0][1]:
            return True
        else:
            return False
    if n > 1:
        for i in range(n):
            if x == ab[i][0] or x == ab[i][1]:
                return True
            else:
                return jump(n-1,x-ab[i][0],ab) or jump(n-1,x-ab[i][1],ab)
    return False
n,x = map(int,input().split())
ab = []
for i in range(n):
    ab.append(list(map(int,input().split())))

if __name__ == '__main__':
    jump()