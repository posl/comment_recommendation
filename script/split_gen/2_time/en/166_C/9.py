def main():
    n,m = map(int,input().split())
    h = [int(i) for i in input().split()]
    a = []
    b = []
    for i in range(m):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    good = 0
    for i in range(n):
        flag = 0
        for j in range(m):
            if a[j] == i+1:
                if h[i] <= h[b[j]-1]:
                    flag = 1
                    break
            elif b[j] == i+1:
                if h[i] <= h[a[j]-1]:
                    flag = 1
                    break
        if flag == 0:
            good += 1
    print(good)
