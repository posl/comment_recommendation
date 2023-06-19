def problems125_a():
    a,b,t = map(int,input().split())
    #print(a,b,t)
    count = 0
    for i in range(1,t+1):
        if i%a == 0:
            count += b
    print(count)

if __name__ == '__main__':
    problems125_a()