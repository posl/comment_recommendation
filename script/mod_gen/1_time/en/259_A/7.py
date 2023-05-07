def problem():
    n,m,x,t,d = map(int, input().split())
    for i in range(m):
        if i < x:
            t += d
    print(t)

if __name__ == '__main__':
    problem()