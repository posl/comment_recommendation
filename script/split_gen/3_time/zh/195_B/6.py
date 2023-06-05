def main():
    a,b,w=map(int,input().split())
    w*=1000
    min_num,max_num=0,0
    for i in range(1,w+1):
        if a*i<=w and w<=b*i:
            if min_num==0:
                min_num=i
            max_num=i
    if min_num==0:
        print('UNSATISFIABLE')
    else:
        print(min_num,max_num)
