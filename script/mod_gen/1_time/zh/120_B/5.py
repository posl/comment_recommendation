def problem120_b():
    a,b,k = map(int,input().split())
    res = []
    for i in range(1,101):
        if a%i==0 and b%i==0:
            res.append(i)
    print(res[-k])

if __name__ == '__main__':
    problem120_b()