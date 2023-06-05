def problem181_b():
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = map(int,input().split())
        sum += (a+b)*(b-a+1)//2
    print(sum)
