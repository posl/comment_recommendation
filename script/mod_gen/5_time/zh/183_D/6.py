def is_ok(n,w,plans):
    plans.sort(key=lambda x:x[0])
    #print(plans)
    ans = 0
    for i in range(n):
        ans += plans[i][2]
        if ans > w:
            return False
    return True
n,w = list(map(int,input().split()))
plans = []
for i in range(n):
    plans.append(list(map(int,input().split())))

if __name__ == '__main__':
    is_ok()