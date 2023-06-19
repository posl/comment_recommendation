def get_num():
    a,b,w = map(int,input().split())
    min_num = 0
    max_num = 0
    for i in range(1,1001):
        if a*i <= 1000*w <= b*i:
            min_num = i
            break
    for i in range(1,1001):
        if a*i <= 1000*w <= b*i:
            max_num = i
    if min_num == 0:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)
get_num()
