def get_input():
    n,k = map(int,input().split())
    sushi = []
    for i in range(n):
        t,d = map(int,input().split())
        sushi.append([t,d])
    return n,k,sushi
