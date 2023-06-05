def main():
    n,m = map(int,input().split())
    b = [list(map(int,input().split())) for _ in range(n)]
    #print(b)
    for i in range(10**7):
        a = [[(i*7+j) for j in range(1,8)] for i in range(10**2)]
        for k in range(10**2):
            for l in range(7):
                if a[k][l] in b:
                    a[k][l] = 0
        if sum(map(sum,a)) == 0:
            print("Yes")
            return
    print("No")
