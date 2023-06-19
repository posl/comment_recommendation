def get_list():
    N = int(input())
    list = []
    for i in range(N):
        t,l,r = map(int,input().split())
        list.append([t,l,r])
    return list
